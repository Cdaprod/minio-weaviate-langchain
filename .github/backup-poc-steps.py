import requests
import time
import json

weaviate_url = "http://localhost:8080"

# Wait for Weaviate to become ready
while True:
    try:
        response = requests.get(f"{weaviate_url}/v1/.well-known/ready")
        if response.status_code == 200:
            print("Weaviate is ready.")
            break
    except requests.ConnectionError:
        print("Waiting for Weaviate to start...")
    time.sleep(5)

# Load the schema into Weaviate
schema_path = "schema.json"
with open(schema_path, 'r') as schema_file:
    schema = json.load(schema_file)
    response = requests.post(f"{weaviate_url}/v1/schema", json=schema)
    print("Schema loaded:", response.json())

# Trigger a backup to S3
backup_data = {"id": "mybackup"}
response = requests.post(f"{weaviate_url}/v1/operations/backup/s3", json=backup_data)
print("Backup triggered:", response.json())

# Optional: Restore from a backup
# Uncomment the following lines to enable restore
# restore_data = {"id": "mybackup"}
# response = requests.post(f"{weaviate_url}/v1/operations/restore/s3", json=restore_data)
# print("Restore initiated:", response.json())