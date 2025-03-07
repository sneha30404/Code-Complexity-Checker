import pytest
from checker.complexity import analyze_file

def test_valid_file():
    results = analyze_file("example.py")
    assert len(results) > 0  # File should return results
    assert results[0]["complexity"] >= 1  # Complexity should be 1 or more

def test_file_not_found():
    results = analyze_file("non_existing.py")
    assert results == []  # Should return empty list

def test_empty_file(tmp_path):
    empty_file = tmp_path / "empty.py"
    empty_file.write_text("")  # Create empty file
    results = analyze_file(str(empty_file))
    assert results == []  # Empty file should return empty list
