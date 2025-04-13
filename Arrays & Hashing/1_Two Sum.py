from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return   []
    
# test cases
solution = Solution()
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),    # Example case
    ([3, 2, 4], 6, [1, 2]),        # Normal case
    ([3, 3], 6, [0, 1]),           # Same element case
    ([1, 2, 3], 6, []),            # No solution case
    ([], 0, []),                   # Empty list case
]
# Run test cases
for i, (nums, target, expected) in enumerate(test_cases):
     result = solution.twoSum(nums, target)
     print(f"Test case {i+1}: nums = {nums}, target = {target}")
     print(f"Expected: {expected}, Got: {result}")
     print(f"{'✓ PASSED' if result == expected else '✗ FAILED'}")
     print("-" * 40)
         

