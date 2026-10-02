class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        A = "".join(sorted(s))
        B = "".join(sorted(t))

        for i in range(0, len(A)):
            if A[i] != B[i]:
                return False
        
        return True
        



                