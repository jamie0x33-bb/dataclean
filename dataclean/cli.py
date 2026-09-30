"""CLI entry point for dataclean."""

import argparse
import sys

from dataclean.parsers import clean_csv


def main():
    parser = argparse.ArgumentParser(description="Clean CSV files")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file")
    parser.add_argument("--dedup", action="store_true", help="Remove duplicate rows")
    parser.add_argument("--strip", action="store_true", help="Strip whitespace")
    parser.add_argument("--drop-empty", action="store_true", help="Drop empty rows")

    args = parser.parse_args()

    try:
        count = clean_csv(
            args.input,
            args.output,
            dedup=args.dedup,
            strip=args.strip,
            drop_empty=args.drop_empty,
        )
        print(f"Wrote {count} rows to {args.output}")
    except FileNotFoundError:
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
