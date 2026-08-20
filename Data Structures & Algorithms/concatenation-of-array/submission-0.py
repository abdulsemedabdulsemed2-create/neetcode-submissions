class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_a = 2 * len(nums)
        new_arr = [0] * len_a


        for i in range(len(nums), len(new_arr)):
            for j in range(0, len(nums)):
                new_arr[j] = nums[j]
            new_arr[i] = nums[i - len(nums)]
            

        return new_arr