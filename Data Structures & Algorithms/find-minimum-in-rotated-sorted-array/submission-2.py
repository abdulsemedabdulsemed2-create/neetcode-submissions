class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = sorted(nums)
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] < min(nums):
                L = mid + 1
            elif nums[mid] > min(nums):
                R = mid - 1
            else:
                return nums[mid]
        return -1

