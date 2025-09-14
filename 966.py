class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def devowel(word: str) -> str:

            pattern = []

            for char in word:

                if char in "aeiou":
                    pattern.append("*")
                else:
                    pattern.append(char)

            return "".join(pattern)

        word_set = set(wordlist)
        lowercase_dict = {}
        vowel_pattern_dict = {}

        for word in wordlist:

            word_lower = word.lower()

            if word_lower not in lowercase_dict:
                lowercase_dict[word_lower] = word

            pattern = devowel(word_lower)

            if pattern not in vowel_pattern_dict:
                vowel_pattern_dict[pattern] = word

        result = []

        for query in queries:

            if query in word_set:
                result.append(query)
                continue

            query_lower = query.lower()

            if query_lower in lowercase_dict:
                result.append(lowercase_dict[query_lower])
                continue

            query_pattern = devowel(query_lower)

            if query_pattern in vowel_pattern_dict:
                result.append(vowel_pattern_dict[query_pattern])
                continue

            result.append("")

        return result