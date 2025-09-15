
import re

def preprocess_text(text: str) -> str:
    # normalize CRLF and multiple blank lines, keep timestamps
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
