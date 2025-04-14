from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasmap = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in hasmap:
                hasmap[sorted_str] = []
            hasmap[sorted_str].append(s)
        return list(hasmap.values())
    
# test cases
solution = Solution()
test_cases = [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),  # Example case
    ([""], [[""]]),  # Single empty string case
    (["a"], [["a"]]),  # Single character case
    (["abc", "bca", "cab"], [["abc", "bca", "cab"]]),  # All anagrams case
    ([], [[]]),  # Empty list case
]

# Run test cases
for i, (strs, expected) in enumerate(test_cases):
     result = solution.groupAnagrams(strs)
     print(f"Test case {i+1}: strs = {strs}")
     print(f"Expected: {expected}, Got: {result}")
     print(f"{'✓ PASSED' if result == expected else '✗ FAILED'}")
     print("-" * 40)
     