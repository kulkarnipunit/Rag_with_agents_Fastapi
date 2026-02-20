def embed_text(text: str):
    return [ord(c) % 10 for c in text][:10]