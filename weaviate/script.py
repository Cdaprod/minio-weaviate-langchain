import weaviate
client = weaviate.Client("http://weaviate:8080")

schema = {
  "classes": [
    {
      "class": "Article",
      "description": "A class to store articles",
      "properties": [
        {"name": "title", "dataType": ["string"], "description": "The title of the article"},
        {"name": "content", "dataType": ["text"], "description": "The content of the article"},
        {"name": "datePublished", "dataType": ["date"], "description": "The date the article was published"},
        {"name": "url", "dataType": ["string"], "description": "The URL of the article"}
      ]
    },
    {
      "class": "Author",
      "description": "A class to store authors",
      "properties": [
        {"name": "name", "dataType": ["string"], "description": "The name of the author"},
        {"name": "articles", "dataType": ["Article"], "description": "The articles written by the author"}
      ]
    }
  ]
}
client.schema.delete_class('Article')
client.schema.delete_class('Author')
client.schema.create(schema)

# JSON data to be Ingested

data = [
    {
        "class": "Article",
        "properties": {
            "title": "LangChain: OpenAI + S3 Loader",
            "content": "This article discusses the integration of LangChain with OpenAI and S3 Loader...",
            "url": "https://blog.min.io/langchain-openai-s3-loader/"
        }
    },
    {
        "class": "Article",
        "properties": {
            "title": "MinIO Webhook Event Notifications",
            "content": "Exploring the webhook event notification system in MinIO...",
            "url": "https://blog.min.io/minio-webhook-event-notifications/"
        }
    },
    {
        "class": "Article",
        "properties": {
            "title": "MinIO Postgres Event Notifications",
            "content": "An in-depth look at Postgres event notifications in MinIO...",
            "url": "https://blog.min.io/minio-postgres-event-notifications/"
        }
    },
    {
        "class": "Article",
        "properties": {
            "title": "From Docker to Localhost",
            "content": "A guide on transitioning from Docker to localhost environments...",
            "url": "https://blog.min.io/from-docker-to-localhost/"
        }
    }
]

for item in data:
    client.data_object.create(
        data_object=item["properties"],
        class_name=item["class"]
    )