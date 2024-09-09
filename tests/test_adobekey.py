import pytest
from pathlib import Path
from deDRM.adobekey import extract_adobe_key

def test_extract_adobe_key():
    # Assuming you have a sample .dat file for testing
    sample_dat_file = Path("tests/dummy-activation.dat")
    expected_key_file = Path("tests/dummy-adobekey.der")

    with open(sample_dat_file, "rb") as f:
        dat_content = f.read()

    result = extract_adobe_key(dat_content)

    # Compare the result with the expected key file
    with open(expected_key_file, "rb") as f:
        expected_key = f.read()

    assert result == expected_key, "Extracted key does not match the expected key"
