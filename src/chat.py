# src/chat.py
import requests
import os
import argparse

def ask_local(question: str):
    url = os.getenv("LOCAL_API_URL", "http://localhost:8000/ask")
    r = requests.post(url, json={"question": question})
    print(r.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", required=True)
    args = parser.parse_args()
    ask_local(args.q)
