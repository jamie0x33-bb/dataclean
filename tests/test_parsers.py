"""Tests for the CSV cleaning module."""

from dataclean.parsers import clean_csv
from conftest import _read_csv


def test_passthrough(sample_csv, output_csv):
    n = clean_csv(sample_csv, output_csv)
    assert n == 4
    rows = _read_csv(output_csv)
    assert rows[0] == ["name", "age", "city"]


def test_dedup(sample_csv, output_csv):
    n = clean_csv(sample_csv, output_csv, dedup=True)
    assert n == 3


def test_strip(sample_csv, output_csv):
    clean_csv(sample_csv, output_csv, strip=True)
    rows = _read_csv(output_csv)
    assert rows[-1] == ["Carol", "35", "Los Angeles"]


def test_drop_empty(sample_csv, output_csv):
    n = clean_csv(sample_csv, output_csv, drop_empty=True)
    assert n == 3


def test_combined(sample_csv, output_csv):
    n = clean_csv(sample_csv, output_csv, dedup=True, strip=True, drop_empty=True)
    assert n == 3
    rows = _read_csv(output_csv)
    assert len(rows) == 4  # header + 3 data rows
