# src/utils/chunk.py
from typing import List, Dict
import math

def chunk_segments_with_timestamps(blocks: List[Dict], chunk_size_words: int = 500, chunk_overlap_words: int = 100) -> List[Dict]:
    """
    blocks: [{'start': '00:00:03', 'end': '00:00:05', 'text': '...'}, ...]
    Returns list of {'start','end','text'}
    Approach: concatenate blocks until approx chunk_size_words, with overlap of chunk_overlap_words.
    """
    # build list of tokens per block
    for b in blocks:
        b["word_count"] = len(b["text"].split())
    chunks = []
    i = 0
    n = len(blocks)
    while i < n:
        curr_words = 0
        texts = []
        start_time = blocks[i]["start"]
        end_time = blocks[i]["end"]
        j = i
        while j < n and curr_words < chunk_size_words:
            texts.append(blocks[j]["text"])
            curr_words += blocks[j]["word_count"]
            end_time = blocks[j]["end"]
            j += 1
        chunk_text = " ".join(texts).strip()
        chunks.append({"start": start_time, "end": end_time, "text": chunk_text})
        # move forward by chunk_size - overlap measured in approximate blocks (we compute by words)
        # find new i such that overlap approx chunk_overlap_words
        overlap_needed = chunk_overlap_words
        if j >= n:
            break
        # walk backwards from j-1 to include overlap
        k = j - 1
        overlap_words = 0
        while k >= 0 and overlap_words < overlap_needed:
            overlap_words += blocks[k]["word_count"]
            k -= 1
        # next start index
        next_i = max(i + 1, k + 1)
        i = next_i
    return chunks
