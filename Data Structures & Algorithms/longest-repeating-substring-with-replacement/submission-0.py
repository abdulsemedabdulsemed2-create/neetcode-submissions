class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        left = 0
        replace = 0
        curr = 0
        maxH = 0
        long = 0

        for right in range(len(s)):
            if s[right] in hash_map:
                hash_map[s[right]] += 1
            else:
                hash_map[s[right]] = 1
            curr = right - left + 1
            maxH = max(hash_map.values())

            replace = curr - maxH
            while replace > k:
                hash_map[s[left]] -= 1
                left += 1
                curr = right - left + 1
                maxH = max(hash_map.values())
                replace = curr - maxH
            long = max(long, curr)
        return long