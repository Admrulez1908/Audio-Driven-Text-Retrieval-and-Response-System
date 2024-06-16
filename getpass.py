import os
from getpass import getpass

os.environ["PINECONE_API_KEY"]= getpass('Enter your Pinecone API key:')
os.environ["PINECONE_ENVIRONMENT"]=getpass('Enter your Pinecone environment name:')
