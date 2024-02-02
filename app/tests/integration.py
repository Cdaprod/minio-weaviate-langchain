# tests/integration.py

import pytest
from main import setup_langchain
from langchain_utils.MinioTool import MinioTool
from langchain_utils.WeaviateTool import WeaviateTool

# Mocking the actual Minio and Weaviate instances would be necessary if you're not testing against live instances
@pytest.fixture
def langchain_environment():
    # Setup a test environment
    # This could be more complex in a real-world scenario, including configuring test instances of MinIO and Weaviate
    minio_tool = MinioTool({'endpoint': 'test-endpoint', 'access_key': 'test', 'secret_key': 'test'})
    weaviate_tool = WeaviateTool({'url': 'http://test-url:8080', 'api_version': 'v1'})
    lc = setup_langchain(minio_tool, weaviate_tool)
    return lc

def test_langchain_with_tools(langchain_environment):
    # Assuming your setup_langchain function or equivalent logic initializes LangChain with the tools
    assert 'minio' in langchain_environment.tools, "LangChain should have MinioTool registered"
    assert 'weaviate' in langchain_environment.tools, "LangChain should have WeaviateTool registered"
    # Here you would add more tests that perform actual operations using the tools through LangChain and validate the results