class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        needMap = {}
        for char in t:
            needMap[char] = 1 + needMap.get(char, 0)

        windowMap = {}
        have = 0
        need = len(needMap)

        result = [-1, -1]
        resultLength = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            windowMap[char] = 1 + windowMap.get(char, 0)

            if char in needMap and windowMap[char] == needMap[char]:
                have += 1

            while have == need:
                windowLength = right - left + 1

                if windowLength < resultLength:
                    result = [left, right]
                    resultLength = windowLength

                leftChar = s[left]
                windowMap[leftChar] -= 1

                if leftChar in needMap and windowMap[leftChar] < needMap[leftChar]:
                    have -= 1

                left += 1

        if resultLength == float("inf"):
            return ""

        leftIndex, rightIndex = result
        return s[leftIndex:rightIndex + 1]