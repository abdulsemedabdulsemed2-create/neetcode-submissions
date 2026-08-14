class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_L = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    nums_L.append(i)
                    nums_L.append(j)
                    return nums_L
                else:
                    j += 1
        i += 1
                


                    
            
        