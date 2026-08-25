class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_sorted = sorted(s)
            t_sorted = sorted(t)
            if s_sorted == t_sorted:
                return True
            else:
                return False
        else:
            return False
#Time Complixity=O(nlogn)
#Space Complixity=O(n)