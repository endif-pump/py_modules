# pylint: disable=C0116,C0114
import pytest

from modules.merge_iterables import merge_iterables


@pytest.mark.parametrize("iterables, expected", [
                        ([[1, 5, 9, ], [2, 5, ], [1, 6, 10, 11, ], ], [1, 1, 2, 5, 5, 6, 9, 10, 11, ]),
                        ([[3, 2, 1, ], [5, 1, ], [11, 2], ], [1, 1, 2, 2, 3, 5, 11, ]),
                        ([[0, 0, ], [0, 0, ], [0, 0, ], ], [0, 0, 0, 0, 0, 0, ]),
                        ([[],[]], []),
                        ([[1, ]], [1, ]),
                        ([(1, 3), (2, 4, 5, )], [1, 2, 3, 4, 5, ]),
                        ])
def test_merge_iterables_positive(iterables, expected: int):
    assert list(merge_iterables(*iterables)) == expected

@pytest.mark.parametrize("iterables, expected", [
                        ([(1, 3), [2, 4, 5, ]], [1, 2, 3, 4, 5, ]),
                        ])
def test_merge_different_types_of_iterables(iterables, expected: int):
    assert list(merge_iterables(*iterables)) == expected
    