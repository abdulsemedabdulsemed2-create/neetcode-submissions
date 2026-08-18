class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_val = numbers[left] + numbers[right]
            if current_val < target:
                left += 1
            elif current_val > target:
                right -= 1
            else:
                return [left + 1, right + 1]
