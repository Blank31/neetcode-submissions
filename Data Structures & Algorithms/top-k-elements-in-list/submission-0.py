class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, v in freqMap.items():
            bucket[v].append(num)

        result = []

        for v in range(len(bucket) -1, 0, -1):
            
            for num in bucket[v]:
                result.append(num) 

                if len(result) == k:
                    return result

        return result