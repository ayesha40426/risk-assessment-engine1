import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("risk_docs")

def add_doc(text):
    collection.add(documents=[text], ids=[str(hash(text))])

def query_docs(query):
    return collection.query(query_texts=[query], n_results=2)