VECTOR_DB = []

def similarity(a, b):
    return sum(x * y for x, y in zip(a, b))


def store_vector(text: str, embedding: list):
    VECTOR_DB.append({
        "text": text,
        "embedding": embedding
    })


def search(query_embedding, top_k=3):
    scored = []

    for item in VECTOR_DB:
        score = similarity(query_embedding, item["embedding"])
        scored.append((score, item["text"]))

    scored.sort(reverse=True)

    return [text for _, text in scored[:top_k]]