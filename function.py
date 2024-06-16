def read_and_split_document(file_path, chunk_size=500):
    with open(file_path, 'r') as file:
        text = file.read()
    sentences = sent_tokenize(text)
    return sentences

    chunks = []
    current_chunk = []
    current_length = 0
    for sentence in sentences:
        if current_length + len(sentence) > chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(sentence)
        current_length += len(sentence)
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks




def store_document_in_pinecone(file_path, chunk_size=500):
    chunks = read_and_split_document(file_path, chunk_size)
    embeddings = embedding_model.encode(chunks)
    pinecone_vectors = [
        (f'chunk_{i}', embedding.tolist(), {'text': chunk})
        for i, (embedding, chunk) in enumerate(zip(embeddings, chunks))
    ]
    index.upsert(vectors=pinecone_vectors, namespace='my_namespace')




def query_vector_db(query):
    query_embedding = embedding_model.encode([query])[0]
    result = index.query(vector=query_embedding.tolist(), top_k=5, namespace='my_namespace')
    return [match['metadata']['text'] for match in result['matches']]





def generate_response(query, context_chunks):
    context = ' '.join(context_chunks)
    input_text = query + " " + context
    inputs = llama_tokenizer.encode(input_text, return_tensors='pt')
    outputs = llama_model.generate(inputs, max_length=150)
    response = llama_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


def transcribe_audio(file_path):
    result = whisper_model.transcribe(file_path)
    return result['text']




def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('response.mp3')
    audio = AudioSegment.from_mp3('response.mp3')
    play(audio)


store_document_in_pinecone('mediumblog1.txt', chunk_size=500)


def handle_query_audio(file_path):
    query = transcribe_audio(file_path)
    context_chunks = query_vector_db(query)
    response = generate_response(query, context_chunks)
    text_to_speech(response)


query = transcribe_audio('Recording (2).wav')
print(transcribe_audio('Recording (2).wav'))


handle_query_audio('/content/Recording (2).wav')
