class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current_length = 0
        max_len = 0
        hash_n = set()

        for right in range(len(s)):
            while s[right] in hash_n:
                hash_n.remove(s[left])
                left += 1
            hash_n.add(s[right])
            current_length = right - left + 1
            max_len = max(current_length, max_len)
        return max_len
