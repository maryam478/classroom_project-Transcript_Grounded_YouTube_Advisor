from src.utils import eval_generation, eval_bertscore, eval_judge

def run_eval():
    print("\n=== Running Evaluation Harness ===")

    results = []

    # Run eval_generation
    try:
        eval_generation.run()
        results.append("✅ eval_generation passed")
    except Exception as e:
        results.append(f"❌ eval_generation failed: {e}")

    # Run eval_bertscore
    try:
        eval_bertscore.run()
        results.append("✅ eval_bertscore passed")
    except Exception as e:
        results.append(f"❌ eval_bertscore failed: {e}")

    # Run eval_judge
    try:
        eval_judge.run()
        results.append("✅ eval_judge passed")
    except Exception as e:
        results.append(f"❌ eval_judge failed: {e}")

    print("\n--- Eval Results Summary ---")
    for r in results:
        print(r)

    if all(r.startswith("✅") for r in results):
        print("\n🎉 All evaluation checks passed!")
    else:
        print("\n⚠️ Some evaluation checks failed. See details above.")

if __name__ == "__main__":
    run_eval()

# ============================OUTPUT===================

# docker compose exec app python src/utils/eval.py


# === Running Evaluation Harness ===

# --- Eval: Generation / Grounding ---
# ✅ Schema test passed
# ✅ Grounding test passed
# ❌ Fallback missing
# Bot actually answered: {'answer': 'The transcript provided does not contain information about the capital of Mars. None of the statements reference a specific capital or related concept. If you have more context or a different transcript that includes information about Mars, please share it!', 'grounding': [{'title': 'hayden.txt', 'start_time': '01:01:32', 'end_time': '01:01:33'}, {'title': 'hayden.txt', 'start_time': '00:44:16', 'end_time': '00:44:18'}, {'title': 'hayden.txt', 'start_time': '00:55:24', 'end_time': '00:55:27'}, {'title': 'hayden.txt', 'start_time': '00:18:52', 'end_time': '00:18:53'}, {'title': 'aprilynne.txt', 'start_time': '00:50:39', 'end_time': '00:50:41'}]}

# --- Eval: BERTScore ---
# Some weights of RobertaModel were not initialized from the model checkpoint at roberta-large and are newly initialized: ['pooler.dense.bias', 'pooler.dense.weight']
# You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
# BERTScore F1: 0.9140
# ✅ BERTScore test passed

# --- Eval: LLM Judge ---
# Judge verdict: yes
# ✅ LLM Judge test passed

# --- Eval Results Summary ---
# ✅ eval_generation passed
# ✅ eval_bertscore passed
# ✅ eval_judge passed

# 🎉 All evaluation checks passed!