class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()

        for x in nums:
            uniques.add(x)

        return len(nums) != len(uniques)