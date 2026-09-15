class utils:
    @staticmethod
    def reversed(number: int) -> int:
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        
        sign = -1 if number < 0 else 1
        reversed_str = str(abs(number))[::-1]
        return sign * int(reversed_str)

    @staticmethod
    def formatter(number: int) -> tuple[str, str]:
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        
        binary_format = bin(number)
        octal_format = oct(number)
        return binary_format, octal_format