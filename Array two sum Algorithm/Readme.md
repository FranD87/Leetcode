# Array two sum Algorithm


# Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may 
# assume that each input would have exactly one solution. Maintain a mapping from each number to its index. Check if 
# target - num has already been found.
# Time - O(n)
# Space - O(n) for the dictionary

# STEP BY STEP:

# 1. Create an empty dictionary called `num_to_index` to maintain a mapping from each number to its index in the `nums` array.
# 2. Iterate through the `nums` array using the `enumerate()` function to access both the index `i` and the number `num` at each iteration.
# 3. Check if the difference between the `target` and the current `num` exists as a key in the `num_to_index` dictionary This is done by using the expression `target - num in num_to_index`.
# 4. If the difference is found in the `num_to_index` dictionary, it means that the pair of numbers that add up to the target has been found. Return the indices corresponding to the two numbers by accessing `num_to_index[target - num]` (the index of the complement) and `i` (the current index).
# 5. If the difference is not found in the dictionary, add the current `num` as a key to the `num_to_index` dictionary with its corresponding index `i` as the value.
# 6. If no solution is found after iterating through the entire `nums` array, return an empty list `[]`.
# 7. The time complexity of this solution is O(n), where n is the length of the `nums` array, because we iterate through the array once.
# 8. The space complexity is O(n) because, in the worst case, the `num_to_index` dictionary can contain all n numbers from the `nums` array.

   


