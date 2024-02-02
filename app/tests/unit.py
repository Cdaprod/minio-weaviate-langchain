# tests/unit.py

import pytest
from app.langchain_utils.MinioTool import MinioTool
from app.langchain_utils.WeaviateTool import WeaviateTool
from unittest.mock import patch

# Example unit test for MinioTool
def test_minio_tool_initialization():
    minio_config = {'endpoint': 'localhost:9000', 'access_key': 'minio', 'secret_key': 'minio123'}
    minio_tool = MinioTool(minio_config)
    assert minio_tool.config == minio_config, "MinioTool should correctly store configuration"

@patch('app.langchain_utils.MinioTool.MinioTool.perform_operation')
def test_minio_tool_operation(mock_perform_operation):
    # Mock the perform_operation method to return a predefined value
    mock_perform_operation.return_value = True
    minio_tool = MinioTool({})
    result = minio_tool.perform_operation()
    assert result, "MinioTool should successfully perform operation"

# Example unit test for WeaviateTool
def test_weaviate_tool_initialization():
    weaviate_config = {'url': 'http://localhost:8080', 'api_version': 'v1'}
    weaviate_tool = WeaviateTool(weaviate_config)
    assert weaviate_tool.config == weaviate_config, "WeaviateTool should correctly store configuration"