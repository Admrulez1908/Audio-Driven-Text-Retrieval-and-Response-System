import os
from pinecone import Pinecone
import pinecone
import time



# Create a Pinecone client instance
pc = pinecone.Pinecone(api_key=os.environ["PINECONE_API_KEY"],environment="us-east-1-aws")

# List the indexes
indexes = pc.list_indexes()

# Print the names of the indexes
print(indexes.names())

api_key = os.environ.get("PINECONE_API_KEY")
env = os.environ.get("PINECONE_ENVIRONMENT")

# Create a Pinecone client instance
pc = pinecone.Pinecone(api_key=api_key, environment=env)

# List the indexes
indexes = pc.list_indexes()

# Print the names of the indexes
print(indexes.names())

print(f"Pinecone API Key: {api_key}")
print(f"Pinecone Environment: {env}")
index_name = 'document-embeddings'
pc = pinecone.Pinecone(api_key=os.environ["PINECONE_API_KEY"], environment="us-east-1-aws")

# List the indexes
indexes = pc.list_indexes()

# Print the names of the indexes
print(indexes.names())

print(indexes)

index=pinecone.Index('document-embeddings', host="https://document-embeddings-rk0gfhw.svc.aped-4627-b74a.pinecone.io")

print(index)
host= "https://document-embeddings-rk0gfhw.svc.aped-4627-b74a.pinecone.io"
print(host) 
