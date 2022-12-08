class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        fre = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    fre[i] += 1
        return fre
