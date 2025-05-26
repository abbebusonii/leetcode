class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        answer = r = 0
        hashset = set()
        for l in range(n):
            while r < n and s[r] not in hashset:
                hashset.add(s[r])
                answer = max(answer, len(hashset))
                r += 1
            hashset.remove(s[l])
        return answer