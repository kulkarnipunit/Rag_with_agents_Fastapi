import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query_embedding, memories):

    scored = []

    for m in memories:
        emb = eval(m.embedding)
        score = cosine_similarity(query_embedding, emb)
        scored.append((score, m))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [m.content for _, m in scored[:5]]


def store_vector(db, user_id, content, embedding):
    from app.models.memory import Memory
    
    memory = Memory(
        user_id=user_id,
        content=content,
        embedding=str(embedding)
    )
    
    db.add(memory)
    db.commit()
    db.refresh(memory)
    
    return memory