class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_fix = 1
        post_fix = 1
        end = [1] * len(nums)
        for i in range(len(nums)):
            end[i] = pre_fix
            pre_fix *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            end[i] *= post_fix
            post_fix *= nums[i]
        return end

        