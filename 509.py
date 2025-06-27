class Solution(object):
    def fib(self, n):
        return int(round((((1 + (5 ** 0.5)) / 2)**n) / (5**0.5)))