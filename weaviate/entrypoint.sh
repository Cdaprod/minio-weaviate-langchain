#!/bin/bash

# Start Weaviate in the background
weaviate start &

# Wait for Weaviate to become ready
while ! curl -s http://localhost:8080/v1/.well-known/ready; do
   sleep 5
done

# Load the schema into Weaviate
curl -X POST -H "Content-Type: application/json" \
     --data @/schema.json http://localhost:8080/v1/schema

# Keep the container running
wait