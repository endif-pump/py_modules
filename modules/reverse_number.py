"""Number Reversal Module"""

def reverse_number(number: int | float, reverse_fraction: bool = False) -> int:
    """
    Reversing numbers like integer or float
    
    :param number: any number
    :param reverse_fraction: flag responsible for fraction reversal for real numbers 
        (ex: True - 12.345 => 21.543, False - 12.345 => 543.21)
    :returns: number reverse
    """
    try:
        def reverse_int(num: int) -> int:
            """Reversing numbers integer"""
            num = abs(int(num))
            reversed_num = 0

            while num > 0:
                remainder = num % 10
                reversed_num = reversed_num * 10 + remainder
                num //= 10

            return reversed_num

        if isinstance(number, float):
            whole_part, fraction_part = str(number).split(".")
            reversed_whole = reverse_int(whole_part)
            reversed_fraction = reverse_int(fraction_part)

            if reverse_fraction:
                return float(f"{reversed_whole}.{reversed_fraction}")

            return float(f"{reversed_fraction}.{reversed_whole}")

        return reverse_int(number)

    except Exception:
        return "Number expected"
