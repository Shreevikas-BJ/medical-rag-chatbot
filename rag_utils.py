from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader
import os

def load_documents_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        # Debug print to check loaded files
        print(f"Loading file: {filename}")
        if filename.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
        elif filename.endswith('.txt'):
            loader = TextLoader(os.path.join(folder_path, filename))
        else:
            print(f"Skipped unsupported file: {filename}")
            continue
        docs = loader.load()
        print(f"Loaded {len(docs)} document chunks from {filename}")
        documents.extend(docs)
    print(f"Total documents loaded: {len(documents)}")
    return documents

def create_vector_store(documents):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.split_documents(documents)
    print(f"Split into {len(split_docs)} chunks for embedding")
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(split_docs, embeddings)
    print("Created FAISS vector store")
    return vector_store
