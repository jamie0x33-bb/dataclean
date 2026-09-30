"""Tests for the CSV cleaning module."""

import csv
import os
import tempfile

from dataclean.parsers import clean_csv


def _write_csv(path, rows):
    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(rows)


def _read_csv(path):
    with open(path, newline="") as f:
        return list(csv.reader(f))


def test_passthrough():
    with tempfile.TemporaryDirectory() as d:
        inp = os.path.join(d, "in.csv")
        out = os.path.join(d, "out.csv")
        _write_csv(inp, [["a", "b"], ["1", "2"], ["3", "4"]])
        n = clean_csv(inp, out)
        assert n == 2
        assert _read_csv(out) == [["a", "b"], ["1", "2"], ["3", "4"]]


def test_dedup():
    with tempfile.TemporaryDirectory() as d:
        inp = os.path.join(d, "in.csv")
        out = os.path.join(d, "out.csv")
        _write_csv(inp, [["x"], ["1"], ["1"], ["2"]])
        n = clean_csv(inp, out, dedup=True)
        assert n == 2


def test_strip():
    with tempfile.TemporaryDirectory() as d:
        inp = os.path.join(d, "in.csv")
        out = os.path.join(d, "out.csv")
        _write_csv(inp, [["col"], ["  hello  "], [" world"]])
        clean_csv(inp, out, strip=True)
        rows = _read_csv(out)
        assert rows[1] == ["hello"]
        assert rows[2] == ["world"]


def test_drop_empty():
    with tempfile.TemporaryDirectory() as d:
        inp = os.path.join(d, "in.csv")
        out = os.path.join(d, "out.csv")
        _write_csv(inp, [["a"], ["data"], [""], ["more"]])
        n = clean_csv(inp, out, drop_empty=True)
        assert n == 2


def test_drop_empty_removes_blank_rows(tmp_path):
    src = tmp_path / "in.csv"
    dst = tmp_path / "out.csv"
    src.write_text("a,b\n1,2\n,\n3,4\n")
    written = clean_csv(str(src), str(dst), drop_empty=True)
    assert written == 3
    assert ",\n" not in dst.read_text()


def test_strip_normalises_surrounding_whitespace(tmp_path):
    src = tmp_path / "in.csv"
    dst = tmp_path / "out.csv"
    src.write_text("a,b\n  1  ,  2  \n")
    clean_csv(str(src), str(dst), strip=True)
    assert "1,2" in dst.read_text()
