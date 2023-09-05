# pylint: disable=C0116,C0114,E0401
import pytest

from modules.reverse_number import reverse_number


@pytest.mark.parametrize("number, expected", [
                        (123, 321),
                        (240000, 42),
                        (0, 0), ])
def test_reverse_number_int(number: int, expected: int):
    assert reverse_number(number) == expected


@pytest.mark.parametrize("number, reverse_fraction, expected", [
                        (12.345, True, 21.543),
                        (12.345, False, 543.21), ])
def test_reverse_number_float(number: int, reverse_fraction: bool, expected: int):
    assert reverse_number(number, reverse_fraction) == expected


@pytest.mark.parametrize("number, expected", [
                        ("12.345", "Number expected"),
                        ("12.345.123", "Number expected"),
                        ("dasda", "Number expected"),
                        (-777, 777), ])
def test_reverse_number_negative(number: str, expected: str):
    assert reverse_number(number) == expected
