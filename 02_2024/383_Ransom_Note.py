# TC == O(nm), SC == O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            idx = magazine.find(ransomNote[i])
            if idx == -1:
                return False
            magazine = magazine[:idx] + magazine[idx + 1 :]
        return True


# TC == O(n + m), SC == O(u)
class SolutionV2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        from collections import defaultdict

        c_counts = defaultdict(int)
        for c in magazine:
            c_counts[c] += 1
        for c in ransomNote:
            if c not in c_counts or c_counts[c] <= 0:
                return False
            else:
                c_counts[c] -= 1
        return True
