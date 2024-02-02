# MinIO-Weaviate-LangChain Integration

A FastAPI application demonstrating a text processing pipeline using Weaviate, MinIO, and LangChain with Docker Compose.

## Features

- MinIO bucket document processing.
- OpenAI LangChain for text analysis.
- Document indexing in Weaviate.
- Docker Compose for easy deployment.

## Prerequisites

- Docker and Docker Compose.

## Quick Start

1. **Clone and Navigate**:
```bash
git clone https://github.com/Cdaprod/minio-weaviate-langchain
cd minio-weaviate-langchain
```

2. **Launch Services**:
```bash
docker-compose down && docker-compose up -d
```

## Usage

- **Endpoints**:
  - Process and index: `POST /process_documents`
  - Query documents: `POST /query`
  - Update: `POST /update/{uuid}`
  - Delete: `DELETE /delete/{uuid}`

- **Example**: Querying Documents
  ```python
  import requests
  response = requests.post('http://localhost:8000/query', json={"query": "your_query_here"})
  print(response.json())
  ```

## Contributing

Contributions are welcome. Please fork the repository and submit pull requests.

## Further Development

Adaptation for Jupyter notebooks and advanced configurations are outlined in the documentation.

---

# GRAVEYARD

This will guide users on how to deploy the application using Docker, which simplifies the setup process by handling dependencies and configurations through Docker containers. Here's an updated version of the `README.md` with Docker Compose deployment instructions:

### README.md

# My FastAPI Application with Langchain, Weaviate, and MinIO Integrations

This FastAPI application demonstrates an integrated text processing pipeline using Weaviate and MinIO. It's designed to efficiently process, store, and retrieve documents through a Dockerized environment.

## Features

- Process documents from a MinIO bucket.
- Use OpenAI's LangChain for advanced text processing.
- Index and manage documents in Weaviate.
- Easy deployment with Docker Compose.

## Requirements

- Docker
- Docker Compose

## Installation and Deployment

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Cdaprod/minio-weaviate-langchain
    cd minio-weaviate-langchain
    ```

2. **Start the Application with Docker Compose**:

    Run the following command to start all services defined in your `docker-compose.yaml`:

    ```bash
    docker-compose up
    ```

    This command will build and start containers for your FastAPI app, Weaviate, and MinIO.

## Proof of Concept

The application showcases the following workflow:

1. **Load Documents from MinIO**: The application retrieves documents stored in a MinIO bucket.

2. **Document Processing**: Documents are processed via LangChain's OpenAI integration.

3. **Indexing in Weaviate**: Processed documents are indexed in Weaviate for full-text search and data retrieval.

4. **API Endpoints**:
    - `POST /process_documents`: Processes and indexes documents from MinIO into Weaviate.
    - `GET /`: Health check endpoint.
    - `POST /index_from_minio`: Indexes documents from MinIO into Weaviate.
    - `POST /query`: Queries documents in Weaviate.
    - `POST /update/{uuid}`: Updates a document in Weaviate.
    - `DELETE /delete/{uuid}`: Deletes a document from Weaviate.

## Example Usage

- **Index Documents from MinIO**:

    ```python
    import requests
    response = requests.post('http://localhost:8000/index_from_minio')
    print(response.json())
    ```

- **Query Documents in Weaviate**:

    ```python
    query = '{"query": "your_query_here"}'
    response = requests.post('http://localhost:8000/query', json=query)
    print(response.json())
    ```

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Further Development for Notebook Environment

To adapt your FastAPI application with Weaviate and MinIO integration for use in a Jupyter notebook, you'll need to structure it as a Python package that can be installed and used interactively. The structure of the package should facilitate easy installation and usage within a notebook environment. 

Here's a basic outline of steps to restructure your application:

### 1. Organize Your Application as a Package

Your project directory might look something like this:

```
minio-weaviate-langchain/
    my_fastapi_lib/
        __init__.py
        main.py
        weaviate_operations.py
        minio_operations.py
        # ... other modules ...
    setup.py
    README.md
    LICENSE
```

In `minio-weaviate-langchain/my_fastapi_lib/__init__.py`, you can import the main components:

```python
from .main import app
from .weaviate_operations import WeaviateOperations
from .minio_operations import load_documents_from_minio
```

### 2. Setup.py for Installation

Your `setup.py` allows the package to be installed via pip. Here's an example:

```python
from setuptools import setup, find_packages

setup(
    name='my_fastapi_lib',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
        'weaviate-client',
        'minio',
        'langchain',
        # ... other dependencies ...
    ],
)
```

### 3. Using the Library in a Jupyter Notebook

Once your library is structured and installable, you can create a Jupyter notebook to demonstrate its usage. For example:

#### Cell 1: Install the library

```python
!pip install git+https://github.com/yourusername/my_fastapi_lib.git
```

#### Cell 2: Import and Initialize Components

```python
from my_fastapi_lib import WeaviateOperations, load_documents_from_minio

# Setup Weaviate and MinIO clients
weaviate_ops = WeaviateOperations(WEAVIATE_ENDPOINT)
minio_documents = load_documents_from_minio(MINIO_BUCKET, MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY)
```

#### Cell 3: Use the Library

```python
# Example operation
for doc in minio_documents:
    processed_doc = process_document(doc)  # Define this function as per your processing logic
    weaviate_ops.index_document(MINIO_BUCKET, "DocumentName", processed_doc)
```

### 4. Documentation and Examples

Provide clear instructions and examples in your `README.md` and include Jupyter notebooks that demonstrate the use of your library.

### 5. Running the FastAPI App

Since the FastAPI app is designed to be run as a server, it might not be directly applicable in a Jupyter notebook for interactive use. Instead, focus on demonstrating how to interact with the server (which could be running locally or remotely) using requests or similar in the notebook.

### Note

Adapting a FastAPI application for use as a library in a Jupyter notebook involves a shift in focus. The interactive notebook environment is more suited for demonstrating API calls to the running FastAPI server, rather than running the server itself within the notebook.

# Directory for Autonomous Agent App

For an autonomous agent application powered by LangChain and designed to operate via CI/CD workflows, the directory structure could be tailored to facilitate automated deployment and execution. Here's a modified directory tree strategy:

```
minio-weaviate-langchain/
│
├── .github/workflows/              # CI/CD workflows for agent deployment and operation
│   ├── agent-deploy.yml            # Workflow for deploying agents
│   ├── agent-run.yml               # Workflow to trigger agent execution
│   └── testing.yml                 # Workflow for testing and validation
│
├── minio/                          # MinIO Docker and configuration
│   └── Dockerfile
│
├── weaviate/                       # Weaviate Docker and configuration
│   └── Dockerfile
│
├── app/                            # LangChain application
│   ├── Dockerfile                  # Dockerfile for LangChain environment
│   ├── agents/                     # Autonomous agents
│   │   ├── agent_1.py              # Agent 1 script
│   │   └── agent_2.py              # Agent 2 script
│   ├── langchain_utils/            # LangChain utilities and tools
│   │   ├── conversation.py
│   │   ├── minio_tool.py
│   │   └── weaviate_tool.py
│   ├── data/                       # Data used by agents
│   │   └── agent_data.json
│   ├── tests/                      # Tests for agents and utilities
│   │   └── test_agents.py
│   └── run_agents.py               # Script to execute agents
│
├── docker-compose.yaml             # Docker Compose for service orchestration
└── README.md                       # Project documentation
```

In this structure:
- **.github/workflows/**: Contains CI/CD workflows specifically for deploying and running autonomous agents.
- **app/agents/**: Dedicated directory for individual autonomous agent scripts.
- **app/data/**: Stores data and configurations specific to each agent's operations.
- **app/run_agents.py**: Central script to initiate the execution of agents, which can be triggered via CI/CD pipelines.
- **tests/**: Expanded to include tests for individual agents and their functionalities.

This revised structure supports the autonomous nature of the agents and their operation via CI/CD workflows, enhancing automation and orchestration of the application.