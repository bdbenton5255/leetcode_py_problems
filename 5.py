class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        start_index = 0
        max_length = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n): 
                dp[i][j] = False

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if max_length < j - i + 1:
                        start_index = i
                        max_length = j - i + 1

        return s[start_index : start_index + max_length]