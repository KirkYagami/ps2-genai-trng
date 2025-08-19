from google.genai import types
import os
from google import genai
from chromadb import Documents, EmbeddingFunction, Embeddings




from langchain_google_genai import GoogleGenerativeAIEmbeddings



GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


# class GeminiEmbeddingFunction(EmbeddingFunction):
#   def __call__(self, input: Documents) -> Embeddings:
#     EMBEDDING_MODEL_ID = "gemini-embedding-001"
#     title = "Custom query"
#     response = client.models.embed_content(
#         model=EMBEDDING_MODEL_ID,
#         contents=input,
#         config=types.EmbedContentConfig(
#           task_type="retrieval_document",
#           title=title
#         )
#     )

#     return response.embeddings[0].values