"""Test fixtures for dataclean."""

import csv

import pytest


@pytest.fixture
def sample_csv(tmp_path):
    """Create a sample CSV with mixed data quality for testing."""
    path = tmp_path / "sample.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "city"])
        writer.writerows([
            ["Alice", "30", "New York"],
            ["Bob", "25", "San Francisco"],
            ["Alice", "30", "New York"],
            ["", "", ""],
            ["  Carol  ", " 35 ", "  Los Angeles  "],
        ])
    return str(path)


@pytest.fixture
def output_csv(tmp_path):
    """Provide a temporary output path."""
    return str(tmp_path / "output.csv")


def _read_csv(path):
    """Read a CSV file and return rows as a list."""
    with open(path, newline="") as f:
        return list(csv.reader(f))
