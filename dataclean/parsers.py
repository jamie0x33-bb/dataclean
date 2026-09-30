"""Core CSV cleaning logic."""

import csv
import io
from typing import Optional


def clean_csv(
    input_path: str,
    output_path: str,
    *,
    dedup: bool = False,
    strip: bool = False,
    drop_empty: bool = False,
    columns: Optional[list[int]] = None,
) -> int:
    """Clean a CSV file and write the result.

    Returns the number of rows written.
    """
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return 0

    header = rows[0]
    data = rows[1:]

    if columns:
        header = [header[i] for i in columns if i < len(header)]
        data = [[r[i] for i in columns if i < len(r)] for r in data]

    if strip:
        data = [[cell.strip() for cell in row] for row in data]

    if drop_empty:
        data = [row for row in data if any(cell for cell in row)]

    if dedup:
        seen = set()
        unique = []
        for row in data:
            key = tuple(row)
            if key not in seen:
                seen.add(key)
                unique.append(row)
        data = unique

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    return len(data)
