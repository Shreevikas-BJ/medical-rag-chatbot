import streamlit as st
import os
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from rag_utils import load_documents_from_folder, create_vector_store
import openai

# Load OpenAI API key securely
openai_api_key = os.getenv("Place your OpenAI API key here")

st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")
st.title("🤖 Medical Chatbot")

# Load and cache vector store
@st.cache_resource
def setup_rag():
    documents = load_documents_from_folder("/Users/shreevikasj/Desktop/Medical_Chatbot/medical_docs")  # adjust path if needed
    return create_vector_store(documents)

vectorstore = setup_rag()

# Setup the LangChain LLM for document-based QA
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2, openai_api_key=openai_api_key)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever(), return_source_documents=True)

# Input
user_input = st.text_input("Ask a medical question:")

# History (optional)
if "history" not in st.session_state:
    st.session_state.history = []

if user_input:
    with st.spinner("Searching documents..."):
        result = qa_chain(user_input)
        answer = result["result"].strip()
        sources = result.get("source_documents", [])

        # If no good answer from RAG, fallback to GPT general knowledge
        if answer.lower().startswith("i don't know") or answer == "":
            with st.spinner("Checking general knowledge..."):
                client = openai.OpenAI(api_key=openai_api_key)
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful medical assistant. Answer responsibly and clearly."},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = completion.choices[0].message.content.strip()
                source_info = "🧠 Answer based on general knowledge."
                sources = []
        else:
            source_info = "📚 Answer based on uploaded documents."

        # Store history
        st.session_state.history.insert(0, (user_input, answer, source_info))

# Show history (most recent first)
if st.session_state.history:
    st.subheader("📜 Chat History")
    for q, a, src in st.session_state.history:
        st.markdown(f"**🧑‍⚕️ You:** {q}")
        st.markdown(f"**🤖 Bot:** {a}")
        st.caption(src)
        st.markdown("---")

# Show sources (if from documents)
if user_input and sources:
    with st.expander("📄 Show source excerpts"):
        for i, doc in enumerate(sources):
            source_name = doc.metadata.get("source", "Unknown")
            st.markdown(f"**Source {i + 1} — {source_name}:**")
            st.write(doc.page_content[:500] + ("..." if len(doc.page_content) > 500 else ""))
