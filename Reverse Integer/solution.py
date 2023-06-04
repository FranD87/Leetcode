class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0    # record if negative and change to positive
        x = abs(x)
        reversed_num = 0

        while x != 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        if reversed_num > 2**31 - 1 or reversed_num < -2**31:    # Check if the reversed number exceeds the
                                                                 # 32-bit signed integer limit
            return 0

        return reversed_num if not negative else -reversed_num


'''Example:

Suppose we have the following input:

```python
x = 123
```

We'll execute the code step by step:

1. Initialize a variable `negative` to False since the input `x` is positive.
2. Take the absolute value of `x` using the `abs()` function, so `x` remains unchanged.
3. Initialize a variable `reversed_num` to 0.
4. Enter the `while` loop since `x` is not 0:
   - In the first iteration, `reversed_num` becomes 3 (0 * 10 + 3 % 10).
   - `x` becomes 12 (123 // 10).
   - In the second iteration, `reversed_num` becomes 32 (3 * 10 + 2 % 10).
   - `x` becomes 1 (12 // 10).
   - In the third iteration, `reversed_num` becomes 321 (32 * 10 + 1 % 10).
   - `x` becomes 0 (1 // 10).
5. Exit the `while` loop since `x` is now 0.
6. The reversed number is 321, so we check if it exceeds the 32-bit signed integer limit. In this case, it doesn't.
7. Return the reversed number 321.

For the input `x = 123`, the code returns the reversed number 321.'''