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

# Sleep for a short period to ensure schema is loaded
sleep 10

# Trigger a backup to S3 (MinIO in this case)
curl -X POST -H "Content-Type: application/json" \
     --data '{"id": "mybackup"}' http://localhost:8080/v1/operations/backup/s3

# Sleep for a period to allow backup to complete
sleep 60

# Optional: Restore from a backup
# Uncomment the following lines to enable restore
sleep 10 # Give some time before restore
curl -X POST -H "Content-Type: application/json" \
     http://localhost:8080/v1/operations/restore/s3/mybackup

# Keep the container running
wait