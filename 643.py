class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        
        max_avg = cur_sum / float(k)

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]

            avg = cur_sum / float(k)
            max_avg = max(max_avg, avg)
        
        return max_avg