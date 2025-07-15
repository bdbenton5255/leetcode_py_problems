class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_length = 0

        for number in nums:
            if number != val:
                nums[new_length] = number
                new_length += 1
        
        return new_length