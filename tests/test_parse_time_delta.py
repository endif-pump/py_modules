# pylint: disable=C0116,C0114
import pytest

from modules.parse_time_delta import parse_time_delta


@pytest.mark.parametrize("value, expected", [
                        ("h", 3600),
                        ("m", 60),
                        ("s", 1),
                        ("1.5s", 1),
                        ("2m", 120),
                        ("0.5h", 1800),
                        ("30", 30),
                        ("1.5", 1),
                        (30, 30), ])
def test_parse_time_delta_positive(value: str, expected: int):
    assert parse_time_delta(value) == expected


@pytest.mark.parametrize("value", ["1a", "a1s", "2mh", "as", "a s", "1s 2m", "", ])
@pytest.mark.parametrize("expected", ["Exception raised", ])
def test_parse_time_delta_negative(value: str, expected: str):
    assert parse_time_delta(value) == expected
