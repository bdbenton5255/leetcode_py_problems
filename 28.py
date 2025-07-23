class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length, needle_length = len(haystack), len(needle)
        for start in range(haystack_length - needle_length + 1):
            if haystack[start : start + needle_length] == needle:
                return start
        return -1