class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1


        while left <= right:
            middle = (right + left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1