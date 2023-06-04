class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1

        return True


    '''STEP BY STEP:

1. The given solution checks whether an integer `x` is a palindrome.
2. Convert the integer `x` to a string `s` using the `str()` function. This allows us to easily compare characters.
3. Initialize two pointers, `left` and `right`, pointing to the first and last characters of the string `s`, 
   respectively.
4. Enter a while loop that continues until `left` becomes greater than or equal to `right`. This loop checks 
   characters from both ends, moving towards the center.
5. Inside the loop:
   - Compare the characters at positions `left` and `right` in the string `s`.
   - If they are not equal, return False since the integer is not a palindrome.
   - Increment `left` by 1 to move towards the center from the left end.
   - Decrement `right` by 1 to move towards the center from the right end.
6. If the loop completes without returning False, it means all pairs of characters were equal, and the integer is a 
   palindrome. Return True.
7. The time complexity of this solution is O(n), where n is the number of digits in the integer `x`. We need to compare 
   each pair of characters, moving towards the center.
8. The space complexity is O(1) since we are not using any extra space beyond a few variables for comparison and 
   iteration.'''