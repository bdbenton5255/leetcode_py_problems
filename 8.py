class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        length_of_string = len(s)
        index = 0

        while index < length_of_string and s[index] == ' ':
            index += 1
            
        if index == length_of_string:
            return 0
        
        sign = -1 if s[index] == '-' else 1
        if s[index] in ['-', '+']:
            index += 1
        
        result = 0
        max_safe_int = (2 ** 31 - 1) // 10

        while index < length_of_string:
            if not s[index].isdigit():
                break
            
            digit = int(s[index])

            if result > max_safe_int or (result == max_safe_int and digit > 7):
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31
            
            result = result * 10 + digit
            index += 1
        
        return sign * result