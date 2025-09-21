from src.utils import eval_generation, eval_bertscore, eval_judge

def run_eval():
    print("\n=== Running Evaluation Harness ===")
    eval_generation.run()
    eval_bertscore.run()
    eval_judge.run()
    print("\n🎉 All evaluation checks passed!")

if __name__ == "__main__":
    run_eval()
