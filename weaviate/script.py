import weaviate
import json

# Initialize Weaviate client
client = weaviate.Client("http://weaviate_server:8080")

# Load and create schema
with open('schema.json', 'r') as file:
    schema = json.load(file)
    client.schema.create(schema)

# Ingest data from data.json
with open('data.json', 'r') as file:
    data = json.load(file)
    for item in data:
        client.data_object.create(item, item['class'])

# Trigger a backup to S3
backup_id = "mybackup"
client.backup.s3.create(backup_id)

# Optional: Restore from the backup
# client.backup.s3.restore(backup_id)