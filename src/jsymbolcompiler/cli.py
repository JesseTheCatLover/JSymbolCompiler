import argparse
from jsymbolcompiler.main import main as run

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--engine-root", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    run(
        args.engine_root,
        args.output
    )