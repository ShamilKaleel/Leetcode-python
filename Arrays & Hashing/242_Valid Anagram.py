class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s)==sorted(t)

# test cases
solution = Solution()
test_cases = [
    ("anagram", "nagaram", True),  # Anagrams
    ("rat", "car", False),         # Not anagrams
    ("", "", True),                # Empty strings
    ("a", "a", True),              # Single character, same
    ("a", "b", False),             # Single character, different
]
# Run test cases
for i, (s, t, expected) in enumerate(test_cases):
     result = solution.isAnagram(s, t)
     print(f"Test case {i+1}: s = '{s}', t = '{t}'")
     print(f"Expected: {expected}, Got: {result}")
     print(f"{'✓ PASSED' if result == expected else '✗ FAILED'}")
     print("-" * 40)
       