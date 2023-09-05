"""Time parsing module"""

import re


def parse_time_delta(time_specifier: str | int) -> int:
    """
    Parses the time difference specifier and returns the time interval in seconds
    
    :param time_specifier: time delta specifier (ex: 30, 30s, 60.5m)
    :returns: time interval in seconds
    """
    time_specifier = str(time_specifier)
    units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
    char = ''.join(re.findall(r'[a-zA-Z]+', time_specifier))
    nums = re.findall(r'\d+\.\d+|\d+', time_specifier)

    try:
        if len(nums) > 1:
            raise ValueError("Incorrect value")

        if not char:
            return int(float(nums[0]))

        if not nums:
            return units[char]

        return int(float(nums[0]) * units[char])

    except Exception:
        return "Exception raised"
