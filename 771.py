class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in s:
                count += 1
        
        return count