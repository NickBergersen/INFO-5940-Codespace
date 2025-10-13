import streamlit as st
import os
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import pypdf as PyPDF2
from io import BytesIO

# cleaning characters
raw_api_key = os.environ.get("API_KEY", "")
api_key_clean = ''.join(char for char in raw_api_key if ord(char) < 128)

client = OpenAI(
    api_key=api_key_clean,
    base_url="https://api.ai.it.cornell.edu",
)

st.title("📝 RAG Document Q&A")

# multiple file upload support
uploaded_files = st.file_uploader(
    "Upload your documents", 
    type=["txt", "pdf"],
    accept_multiple_files=True
)

question = st.chat_input(
    "Ask something about the documents",
    disabled=not uploaded_files,
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Upload documents and ask questions!"}]

# new session state variables for RAG
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# PDF extraction function
def extract_text_from_pdf(file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

# processing with chunking and vector store
def process_documents(files):
    """Process documents and create vector store with chunking"""
    all_text = ""
    
    # extract text from files
    for file in files:
        if file.name.endswith('.txt'):
            all_text += file.read().decode("utf-8") + "\n\n=== New Document ===\n\n"
        elif file.name.endswith('.pdf'):
            all_text += extract_text_from_pdf(file) + "\n\n=== New Document ===\n\n"
    
    # chunk splitting
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(all_text)
    
    # embeddings and vector store
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings
    )
    
    return vectorstore

# process uploaded files
if uploaded_files:
    current_files = [f.name for f in uploaded_files]
    
    # Only reprocess if files changed
    if current_files != st.session_state.processed_files:
        with st.spinner("Processing documents..."):
            st.session_state.vectorstore = process_documents(uploaded_files)
            st.session_state.processed_files = current_files
            
        st.success(f"✅ Processed {len(uploaded_files)} document(s)!")

# RAG-based question handling with retrieval
if question and st.session_state.vectorstore:
    # cleaning
    question_clean = question.encode('ascii', 'ignore').decode('ascii')
    
    st.session_state.messages.append({"role": "user", "content": question_clean})
    st.chat_message("user").write(question)
    
    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            # Retrieve relevant chunks from vector store
            docs = st.session_state.vectorstore.similarity_search(question, k=4)
            context = "\n\n".join([doc.page_content for doc in docs])
            
            # cleaning
            context = context.encode('ascii', 'ignore').decode('ascii')
            
            # cleaning
            clean_messages = []
            for msg in st.session_state.messages:
                clean_content = msg["content"].encode('ascii', 'ignore').decode('ascii')
                clean_messages.append({"role": msg["role"], "content": clean_content})
            
            # response
            stream = client.chat.completions.create(
                model="openai.gpt-4o",
                messages=[
                    {"role": "system", "content": f"Answer based on this context:\n\n{context}"},
                    *clean_messages
                ],
                stream=True
            )
            response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})