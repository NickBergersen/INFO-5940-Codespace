# Reference Log - Assignment 1

## External Sources and Tools Used

### Documentation
- **LangChain Documentation** (https://python.langchain.com/docs/) - For RAG pipeline implementation, text splitters, embeddings, and vector stores
- **Streamlit Documentation** (https://docs.streamlit.io/) - For building the web interface and file upload functionality
- **pypdf Documentation** (https://pypdf2.readthedocs.io/) - For PDF text extraction
- **ChromaDB Documentation** (https://docs.trychroma.com/) - For vector database setup
- **HuggingFace Sentence Transformers** (https://www.sbert.net/) - For the embedding model (all-MiniLM-L6-v2)

### Libraries
- streamlit, langchain, langchain_community, chromadb, sentence-transformers, pypdf, openai

### Course Resources
- Course GitHub repository (assignment1 branch) - Starting template: `chat_with_pdf.py`

## GenAI Usage

### Claude AI (Anthropic)
**Usage 1**: Debugging Pydantic version conflicts with OpenAI embeddings  
**Rationale**: Suggested switching to HuggingFace embeddings to avoid compatibility issues

**Usage 2**: Resolving UnicodeEncodeError  
**Rationale**: Provided text cleaning solution using `.encode('ascii', 'ignore').decode('ascii')`

**Usage 3**: PDF library selection and syntax  
**Rationale**: Recommended pypdf library and provided implementation examples for PDF text extraction

**Usage 4**: General debugging assistance  
**Rationale**: Quick troubleshooting for errors and syntax clarification throughout development