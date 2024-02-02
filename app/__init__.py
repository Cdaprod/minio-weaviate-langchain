
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

import getpass
import os
import uuid


def _set_if_undefined(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass(f"Please provide your {var}")


_set_if_undefined("OPENAI_API_KEY")
_set_if_undefined("LANGCHAIN_API_KEY")
_set_if_undefined("TAVILY_API_KEY")

# Optional, add tracing in LangSmith.
# This will help you visualize and debug the control flow
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Multi-agent Collaboration"