# Medical RAG Chatbot

A Retrieval-Augmented Generation chatbot that answers health-related questions by retrieving information from trusted medical documents using **FAISS** and **GPT-based response generation**.

This project demonstrates how RAG can be used to build a domain-specific chatbot that grounds responses in uploaded medical reference documents instead of relying only on general LLM knowledge.

---

## Overview

Medical questions require careful and reliable responses. General-purpose chatbots may provide answers that sound confident but are not always grounded in trusted sources.

This project builds a medical document-based chatbot that retrieves relevant context from local medical documents and uses that context to generate helpful answers.

The system combines:

- Document loading from a local medical knowledge folder
- Text chunking for better retrieval
- Embedding generation
- FAISS vector search
- GPT-based answer generation
- Fallback LLM reasoning when document context is limited

The goal is to demonstrate a practical healthcare-focused RAG pipeline for document-based question answering.

---

## Problem Statement

Users often ask medical or health-related questions in natural language, but reliable answers should be grounded in trusted references.

This project addresses questions such as:

- Can a chatbot retrieve relevant medical information from local documents?
- Can FAISS be used to search trusted medical content efficiently?
- Can GPT generate understandable answers using retrieved context?
- How can a medical chatbot avoid relying only on general model knowledge?
- How can document-grounded AI improve trust and usability?

---

## Key Features

- Medical question-answering chatbot
- Retrieval-Augmented Generation pipeline
- Local medical document ingestion
- Semantic search using FAISS
- GPT-based response generation
- Context-aware answers from trusted documents
- Fallback LLM reasoning when retrieval context is weak
- Python-based modular implementation
- Simple app interface using `app.py`
- Separate utility module for RAG logic

---

## Tech Stack

| Category | Tools / Libraries |
|---|---|
| Language | Python |
| RAG Pipeline | Custom RAG utilities |
| Vector Search | FAISS |
| LLM | GPT / OpenAI API |
| Embeddings | OpenAI Embeddings or compatible embedding model |
| Document Processing | Local document loading |
| App Logic | Python |
| Core Files | `app.py`, `rag_utils.py` |

---

## Repository Structure


    medical-rag-chatbot/
    │
    ├── medical_docs/
    │   └── Trusted medical documents used for retrieval
    │
    ├── app.py
    │   └── Main application file
    │
    ├── rag_utils.py
    │   └── Core RAG functions for loading, chunking, embedding, retrieval, and response generation
    │
    ├── Requirements.txt
    │   └── Python dependencies
    │
    └── README.md

## System Workflow

    User Medical Question
            ↓
    Load Trusted Medical Documents
            ↓
    Split Documents into Text Chunks
            ↓
    Generate Embeddings
            ↓
    Store Embeddings in FAISS Vector Index
            ↓
    Retrieve Relevant Medical Context
            ↓
    Generate GPT-Based Answer
            ↓
    Return Context-Aware Response
    
## How It Works

**1. Medical Document Loading**

The chatbot uses files stored inside the medical_docs/ folder as the trusted knowledge source.

These documents act as the reference material for answering user questions.

**2. Text Chunking**

Long medical documents are split into smaller chunks.

Chunking improves retrieval quality because the system can search for the most relevant sections instead of passing entire documents to the model.

**3. Embedding Generation**

Each text chunk is converted into a numerical vector representation using an embedding model.

These embeddings help the system compare user questions with document content based on meaning, not just keyword matching.

**4. FAISS Vector Search**

FAISS stores the document embeddings and performs fast similarity search.

When a user asks a question, the system retrieves the most relevant medical document chunks.

**5. GPT Response Generation**

The retrieved context is passed to a GPT-based model to generate a natural-language answer.

The answer is based on the retrieved medical content, making it more grounded than a generic chatbot response.

**6. Fallback Reasoning**

If the retrieved context is limited, the system can use fallback LLM reasoning to still provide a general response.

This helps improve usability while keeping the main pipeline document-grounded.

## Example Use Case

User Question
What are common symptoms of diabetes?
System Behavior

The chatbot searches the medical documents for diabetes-related content, retrieves the most relevant chunks, and generates an answer based on that information.

Example Output
Common symptoms of diabetes may include increased thirst, frequent urination, fatigue, blurred vision, and unexplained weight changes. Please consult a qualified healthcare professional for diagnosis or treatment.

## Important Medical Disclaimer

This project is for educational and portfolio purposes only.

It is not a medical device, diagnostic tool, or substitute for professional medical advice.

Users should always consult a licensed healthcare professional for medical concerns, diagnosis, treatment, prescriptions, or emergency care.

## Getting Started

**1. Clone the Repository**
git clone https://github.com/Shreevikas-BJ/medical-rag-chatbot.git
cd medical-rag-chatbot

**2. Create a Virtual Environment**
python -m venv venv

Activate the environment:

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate

**3. Install Dependencies**

pip install -r Requirements.txt

## Environment Variables

If the project uses OpenAI or another hosted LLM provider, create a .env file in the project root and add your API key:

    OPENAI_API_KEY=your_openai_api_key_here

Do not commit your .env file to GitHub.

## Add Medical Documents

Place trusted medical documents inside the medical_docs/ folder.

Example:

    medical_docs/
    │
    ├── diabetes_overview.pdf
    ├── hypertension_guide.pdf
    ├── first_aid_reference.pdf
    └── general_health_notes.txt

The chatbot will use these documents as its retrieval source.

## Run the Application

    python app.py

If the app is built with Streamlit, use:

    streamlit run app.py

If the app uses Flask or another framework, update the run command based on the implementation.

## Recommended Repository Description

RAG-based medical chatbot using FAISS and GPT to retrieve health-related answers from trusted medical documents with fallback LLM reasoning.

## Business and Technical Value

This project demonstrates how RAG can be applied in healthcare-adjacent use cases where answers should be grounded in reference documents.

Potential use cases include:

Medical document Q&A
Healthcare knowledge assistants
Patient education support
Clinical training document search
Internal healthcare policy lookup
First-aid or wellness information retrieval

## Key Learnings

This project helped strengthen:

Retrieval-Augmented Generation design
Vector search using FAISS
Medical document ingestion
Text chunking and embedding workflows
GPT-based response generation
Domain-specific chatbot development
Responsible AI considerations in healthcare-related systems
Modular Python project structure

## Future Improvements
Add citation-based answers with document names and page numbers
Add similarity threshold gating to reduce hallucinations
Add refusal handling when documents do not contain enough information
Add support for PDF, DOCX, TXT, and web-based medical sources
Add Streamlit or Flask UI improvements
Add chat history
Add document upload through the interface
Add source filtering by topic or document type
Add medical safety guardrails
Add evaluation metrics for retrieval quality
Add Docker support
Deploy the app on Streamlit Community Cloud, Render, or AWS
Add a .gitignore file to exclude cache and environment files
## Suggested .gitignore

    __pycache__/
    *.pyc
    .env
    venv/
    .venv/
    .DS_Store
    *.log
    faiss_index/

## Author

Shreevikas Bangalore Jagadish
Graduate Student, Information Technology and Management
Illinois Institute of Technology

GitHub: Shreevikas-BJ
LinkedIn: shreevikasbj
Portfolio: datascienceportfol.io/shreevikasbj

## Repository

    https://github.com/Shreevikas-BJ/medical-rag-chatbot  
