class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
#Time Complixity=O(n)
#Space Complixity=O(1)