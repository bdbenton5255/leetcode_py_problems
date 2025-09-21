class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if divisor == 1:
            return dividend

        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor

        quotient = 0

        while dividend <= divisor: 
            current_divisor = divisor
            current_quotient = 1

            while current_divisor >= -(2**30) and dividend <= (current_divisor << 1):
                current_divisor <<= 1  # Multiply by 2
                current_quotient <<= 1  # Multiply by 2

            dividend -= current_divisor
            quotient += current_quotient

        return quotient if is_positive else -quotient