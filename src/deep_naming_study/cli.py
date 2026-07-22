import argparse, json
from pathlib import Path
from .study import scaffold_study, validate_study


def main() -> int:
    parser = argparse.ArgumentParser(prog="deep-naming-study")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init"); init.add_argument("brief"); init.add_argument("destination")
    check = sub.add_parser("check"); check.add_argument("study")
    args = parser.parse_args()
    if args.command == "init":
        print(scaffold_study(json.loads(Path(args.brief).read_text()), args.destination))
        return 0
    errors = validate_study(args.study)
    for error in errors: print(f"ERROR: {error}")
    print("RESULT: PASS" if not errors else "RESULT: FAIL")
    return 0 if not errors else 1


if __name__ == "__main__": raise SystemExit(main())
