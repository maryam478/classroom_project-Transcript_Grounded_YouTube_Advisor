from bert_score import score

def run():
    print("\n--- Eval: BERTScore ---")
    cands = ["Start strong with your title in the intro."]
    refs = ["Make sure your intro clearly reflects your title."]
    P, R, F1 = score(cands, refs, lang="en", verbose=False)
    print(f"BERTScore F1: {F1.mean().item():.4f}")
    assert F1.mean().item() > 0.7, "❌ Low similarity score"
    print("✅ BERTScore test passed")
