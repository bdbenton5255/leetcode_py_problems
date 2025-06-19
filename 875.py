class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, int(1e9)

        while left < right:
            mid = (left + right) >> 1
            total_hours = sum((pile + mid - 1) // mid for pile in piles)
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left