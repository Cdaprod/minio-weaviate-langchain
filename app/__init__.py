from .main import app
from .weaviate_operations import WeaviateOperations
from .minio_operations import load_documents_from_minio
# main.py or any other Python file

# Import the config module
import llm_config

# Use the variables
lmstudio_api_key = llm_config.LMSTUDIO_API_KEY
lmstudio_endpoint = llm_config.LMSTUDIO_ENDPOINT
openai_api_key = llm_config.OPENAI_API_KEY

LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=""
LANGCHAIN_PROJECT="minio-weaviate-langchain"