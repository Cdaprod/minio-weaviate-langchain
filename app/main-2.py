# %%capture --no-stderr
# %pip install -U langgraph langchain langchain_openai langchain_experimental

from fastapi import FastAPI
from langchain.llms import OpenAI
from langchain.runnables import Runnable
from langchain import add_routes

from .weaviate_operations import WeaviateOperations
from .minio_operations import load_documents_from_minio

# Weaviate and MinIO connection details
WEAVIATE_ENDPOINT = "http://weaviate:8080"
MINIO_ENDPOINT = "play.min.io:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
MINIO_BUCKET = "web-documentation"

app = FastAPI()

class DocumentProcessingRunnable(Runnable):
    def __init__(self):
        self.llm = OpenAI()
        self.weaviate_ops = WeaviateOperations(WEAVIATE_ENDPOINT)
        self.bucket_name = MINIO_BUCKET
        self.minio_ops = lambda: load_documents_from_minio(self.bucket_name, MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY)

    def run(self, _):
        documents = self.minio_ops()

        for doc in documents:
            processed_doc = self.process_document(doc)
            doc_name = self.extract_document_name(processed_doc)
            self.weaviate_ops.index_document(self.bucket_name, doc_name, processed_doc)

    def process_document(self, document):
        prompt = f"Process this document: {document}"
        response = self.llm.complete(prompt=prompt)
        return response

    def extract_document_name(self, document):
        return "ExtractedDocumentName"

runnable = DocumentProcessingRunnable()

add_routes(app, runnable, path="/process_documents")

@app.get("/")
async def root():
    return {"message": "LangChain-Weaviate-MinIO Integration Service"}
    
@app.post("/index_from_minio")
async def index_from_minio():
    runnable.run(None)
    return {"status": "Indexing complete"}

@app.post("/query")
async def query_weaviate(query: str):
    return runnable.weaviate_ops.query_data(query)

@app.post("/update/{uuid}")
async def update_document(uuid: str, update_properties: dict):
    runnable.weaviate_ops.update_document(uuid, update_properties)
    return {"status": "Document updated"}

@app.delete("/delete/{uuid}")
async def delete_document(uuid: str):
    runnable.weaviate_ops.delete_document(uuid)
    return {"status": "Document deleted"}