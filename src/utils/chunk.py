def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50):
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - chunk_overlap
    return chunks
