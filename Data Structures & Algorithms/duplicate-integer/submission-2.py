class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        conjunto = set()
        for i in nums:
            if i in conjunto:
                return True
            conjunto.add(i)
        return False