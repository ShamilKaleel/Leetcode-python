import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store value -> index pairs
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // Loop through the array
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Check if the complement is already in the map
            if (map.containsKey(complement)) {
                // If found, return the indices
                return new int[] { map.get(complement), i };
            }
            
            // Otherwise, put the current number with its index into the map
            map.put(nums[i], i);
        }
        
        // Just in case there's no solution, though problem guarantees one
        throw new IllegalArgumentException("No two sum solution");
    }
}
