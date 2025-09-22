from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_count = Counter(words)
        string_length = len(s)
        num_words = len(words)
        word_length = len(words[0])
        result = []

        for start_pos in range(word_length):
            left = right = start_pos
            current_word_count = Counter()

            while right + word_length <= string_length:
                current_word = s[right:right + word_length]
                right += word_length

                if word_count[current_word] == 0:
                    left = right
                    current_word_count.clear()
                    continue

                current_word_count[current_word] += 1

                while current_word_count[current_word] > word_count[current_word]:
                    removed_word = s[left:left + word_length]
                    left += word_length
                    current_word_count[removed_word] -= 1

                if right - left == num_words * word_length:
                    result.append(left)

        return result