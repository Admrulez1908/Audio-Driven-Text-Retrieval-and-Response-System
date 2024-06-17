# RAG Model with audio interface using Llama 3b model

This project demonstrates how to store data from a text file (e.g., a book) into Pinecone using Llama 3b and SentenceTransformer for embedding. The script reads a book, splits it into manageable chunks, generates embeddings for each chunk, and stores them in a Pinecone vector store to solve the queries.

## Requirements

- Python 3.6+
- Pinecone API key

## Installation

1. Clone the repository:
   ```bas
   git clone https://github.com/yourusername/book-embedding-storage.git
   cd book-embedding-storage

2. Install the required libraries
   ```bas
   pip install pinecone-client langchain openai nltk

## Setup

1. Set up your environment variables for Pinecone and OpenAI:
   ```cmd
   set PINECONE_API_KEY="your_pinecone_api_key"
   set PINECONE_ENVIRONMENT="your_pinecone_environment"
   set OPENAI_API_KEY="your_openai_api_key"

2. Replace path/to/your/book.txt with the path to your text file in the script.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
1. Fork the repository
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request
   



