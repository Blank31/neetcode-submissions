from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        am = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                freq[index] += 1

            key = tuple(freq)

            am[key].append(word)

        return list(am.values())

