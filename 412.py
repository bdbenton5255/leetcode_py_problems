class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for nums in range(1, n+1):
            if nums % 15 == 0:
                ans.append('FizzBuzz')
            elif nums % 3 == 0:
                ans.append('Fizz')
            elif nums % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(nums))
        return ans