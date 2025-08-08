class Solution:
    def reverse(self, x: int) -> int:
        reversed_number = 0
        min_int, max_int = -2**31, 2**31 - 1
        
        while x:
            if reversed_number < min_int // 10 + 1 or reversed_number > max_int // 10:
                return 0
            
            digit = x % 10
            
            if x < 0 and digit > 0:
                digit -= 10
            
            reversed_number = reversed_number * 10 + digit

            x = (x - digit) // 10
        
        return reversed_number