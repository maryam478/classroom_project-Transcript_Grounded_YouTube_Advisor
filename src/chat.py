import argparse
from pipeline import ask

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=str, required=True, help="Question to ask")
    args = parser.parse_args()

    print(ask(args.q))
