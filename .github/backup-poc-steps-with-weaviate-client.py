import weaviate
import json

# Initialize Weaviate client
client = weaviate.Client("http://localhost:8080")

# Load the schema into Weaviate
schema_path = "schema.json"
with open(schema_path, 'r') as schema_file:
    schema = json.load(schema_file)
    client.schema.create_class(schema['classes'][0])  # Assuming one class in the schema

# Trigger a backup to S3
backup_data = {"id": "mybackup"}
client.backup.create(backup_data)

# Optional: Restore from a backup
# Uncomment the following line to enable restore
# client.restore.create("mybackup")