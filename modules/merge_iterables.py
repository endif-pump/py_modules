"""Iterator Consolidation Module"""

from typing import Iterable, Any, Generator

from numpy import sort

def merge_iterables(*iterables: Iterable[Any]) -> Generator:
    """
    Combining and sorting iterators
    
    :param iterables: iterable objects
    :return: generator that yields sorted values from the input iterables
    """
    iterators = [iter(sort(list(itr))) for itr in iterables]
    current_values = [next(itr, None) for itr in iterators]

    while any(value is not None for value in current_values):
        min_value = min(value for value in current_values if value is not None)
        yield min_value

        min_index = current_values.index(min_value)
        current_values[min_index] = next(iterators[min_index], None)
        

