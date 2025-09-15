class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        broken_letters_set = set(brokenLetters)
        words = text.split()
        typeable_count = 0

        for word in words:

            can_type_word = True

            for char in word:
                if char in broken_letters_set:
                    can_type_word = False
                    break

            if can_type_word:
                typeable_count += 1

        return typeable_count