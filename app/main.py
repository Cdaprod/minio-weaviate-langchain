# main.py

import sys
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
# Assuming LangChain core functionalities are similarly structured
from langchain_core import LangChain
# For runnables, tools, and creating agents, adjust according to the new package structure
from langchain_runnables import Runnable
from langchain_tools import BaseTool
# Example for creating an OpenAI functions agent, adjust the import based on actual package structure and naming
from langchain_agents import create_openai_functions_agent
# Adjust the imports based on your project structure
from config import app_config, langchain_config, llm_config, tool_config
from langchain_utils.MinioTool import MinioTool
from langchain_utils.WeaviateTool import WeaviateTool
from weaviate_operations import WeaviateOperations
from minio_operations import load_documents_from_minio

# Weaviate and MinIO connection details, ensure these are correctly configured
WEAVIATE_ENDPOINT = "http://weaviate:8080"
MINIO_ENDPOINT = "minio:9000"
MINIO_ACCESS_KEY = "minio"
MINIO_SECRET_KEY = "minio123"
MINIO_BUCKET = "langchain-bucket"

app = FastAPI()

class DocumentProcessingRunnable(Runnable):
    def __init__(self, minio_tool, weaviate_tool):
        self.llm = ChatOpenAI(api_key=llm_config.API_KEY)
        self.weaviate_ops = WeaviateOperations(weaviate_tool.config['url'])
        self.bucket_name = MINIO_BUCKET
        self.minio_ops = lambda: load_documents_from_minio(self.bucket_name, minio_tool.config['endpoint'], minio_tool.config['access_key'], minio_tool.config['secret_key'])

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

def initialize_tools():
    """
    Initialize and return instances of MinioTool and WeaviateTool.
    """
    minio_tool = MinioTool(tool_config.MINIO_CONFIG)
    weaviate_tool = WeaviateTool(tool_config.WEAVIATE_CONFIG)
    return minio_tool, weaviate_tool

def setup_document_processing_runnable():
    """
    Setup DocumentProcessingRunnable with MinioTool and WeaviateTool.
    """
    minio_tool, weaviate_tool = initialize_tools()
    runnable = DocumentProcessingRunnable(minio_tool, weaviate_tool)
    return runnable

runnable = setup_document_processing_runnable()

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
