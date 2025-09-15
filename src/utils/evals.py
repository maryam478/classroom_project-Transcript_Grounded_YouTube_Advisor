# eval.py
import requests

API = "http://localhost:8000/ask"
EXAMPLES = [
    ("How should I write the first sentence so viewers feel they got what they clicked for?", "aprilynne.txt"),
    ("How can I improve storytelling to keep longer retention?", "hayden.txt"),
    ("What's the weather in London?", None),
]

def run():
    for q, expected_file in EXAMPLES:
        r = requests.post(API, json={"question": q}).json()
        answer = r.get("answer","")
        grounding = r.get("grounding", [])
        print("\nQUESTION:", q)
        print("ANSWER:", answer)
        print("GROUNDING:", grounding)
        if expected_file:
            ok = any(expected_file in g.get("title","") for g in grounding)
            print("Expected grounding present:", ok)
        else:
            print("Out of domain — expected empty grounding or I don't know ->", not grounding or "don't know" in answer.lower())

if __name__ == "__main__":
    run()
