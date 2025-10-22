Utilized Claude AI to help debug issues/errors.

Ran into issues with OpenAI embeddings and Claude suggested to switch to HuggingFace embeddings from Langchain to avoid compatibility issues from Pydantic version conflicts.

'UnicodeEncodeError' error debug so implemented a text cleaning line (.encode('ascii', 'ignore').decode('ascii')).

For PDF processing I asked what library would best fit and pypdf library was suggested. Looked up syntax to implement into application.