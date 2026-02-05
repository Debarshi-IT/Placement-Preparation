class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        threshold = len(nums) // 3
        for num in nums:
            current_count = freq.get(num, 0)
            freq[num] = current_count + 1
        for num, count in freq.items():
            if count > threshold:
                res.append(num)
        return res
