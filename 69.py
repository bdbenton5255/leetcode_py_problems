class Solution:
    def mySqrt(self, x: int) -> int:
        left_boundary, right_boundary = 0, x

        while left_boundary < right_boundary:
            mid = (left_boundary + right_boundary + 1) >> 1

            if mid <= x // mid:
                left_boundary = mid
            else:
                right_boundary = mid - 1
        
        return left_boundary