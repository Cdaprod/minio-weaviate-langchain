# Stage 1: Install Python and Weaviate client in a temporary image
FROM python:3.8-slim as python-base
RUN pip install --upgrade weaviate-client

# Stage 2: Use the official Weaviate image
FROM semitechnologies/weaviate:latest

# Copy Python runtime and Weaviate client from the python-base stage
COPY --from=python-base /usr/local /usr/local

# Copy the script into the container
COPY script.py /weaviate/script.py

# Custom entrypoint to run the script
ENTRYPOINT ["sh", "-c", "weaviate start & python /weaviate/script.py"]