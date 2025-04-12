from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# Create an instance of the Solution class
solution = Solution()

# Define test cases
test_cases = [
    ([1, 2, 3, 1], True),          # Contains duplicate 1
    ([1, 2, 3, 4], False),         # No duplicates
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),  # Multiple duplicates
    ([], False)                     # Empty array
]

# Run test cases
for i, (nums, expected) in enumerate(test_cases):
    result = solution.containsDuplicate(nums)
    print(f"Test case {i+1}: nums = {nums}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"{'✓ PASSED' if result == expected else '✗ FAILED'}")
    print("-" * 40)