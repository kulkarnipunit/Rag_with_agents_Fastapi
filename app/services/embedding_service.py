from sentence_transformers import SentenceTransformer

# load once (singleton)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text: str):
    """
    Convert text into vector embedding
    """
    embedding = model.encode(text).tolist()
    return embedding