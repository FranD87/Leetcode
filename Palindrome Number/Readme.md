# Determine whether an integer is a palindrome. Do this without extra space.

# Check equivalence of first and last characters, moving inwards.
# Time - O(n)
# Space - O(1)


# 1. To determine whether an integer is a palindrome, we can compare the first and last characters, moving inwards towards the center of the number.
# 2. Convert the integer to a string for easier comparison of characters.
# 3. Initialize two pointers, `start` and `end`, pointing to the first and last characters of the string representation of the integer, respectively.
# 4. While `start` is less than or equal to `end`, perform the following steps:
    - Compare the characters at positions `start` and `end`.
    - If they are not equal, return False as the integer is not a palindrome.
    - Move `start` one step forward and `end` one step backward to continue checking the next pair of characters towards the center.
# 5. If the loop completes without returning False, it means all pairs of characters were equal, and the integer is a palindrome. Return True.
# 6. The time complexity of this solution is O(n), where n is the number of digits in the integer. We need to compare each pair of characters, moving towards the center.
# 7. The space complexity is O(1) since we are not using any extra space beyond a few variables for comparison and iteration.