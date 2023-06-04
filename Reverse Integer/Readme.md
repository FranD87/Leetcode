# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Repeatedly multiply previous result by 10 and add last digit.
# Time - O(n) where n is the number of digits.
# Space - O(n), same number of digits in output as input.


# 1. To reverse the digits of an integer `x`, we can repeatedly multiply the previous result by 10 and add the last 
   # digit of `x`.
# 2. Start by initializing a variable `reversed_num` to 0. This variable will store the reversed number.
# 3. Check if `x` is negative. If it is, record this information by setting a boolean variable `negative` to True and 
   # change `x` to its absolute value using the `abs()` function.
# 4. Enter a while loop that continues until `x` becomes 0.
# 5. Inside the loop:
    # - Multiply `reversed_num` by 10 and add the last digit of `x` by calculating `reversed_num * 10 + x % 10`.
    # - Update `x` by performing an integer division `x //= 10` to remove the last digit.
# 6. Once the loop exits, check if the reversed number `reversed_num` exceeds the 32-bit signed integer limit (2^31 - 1) 
   # or is less than the negative limit (-2^31). If it does, return 0 to comply with the requirements.
# 7. Finally, return `reversed_num` if the original input `x` was positive or return `-reversed_num` if it was negative.
# 8. The time complexity of this solution is O(n), where n is the number of digits in the input `x`. This is because we 
   # iterate through each digit once.
# 9. The space complexity is O(n) since the number of digits in the output `reversed_num` will be the same as the number 
   # of digits in the input `x`.