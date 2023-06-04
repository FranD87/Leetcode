class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_index = {}           # key is number, value is index in nums

        for i, num in enumerate(nums):

            if target - num in num_to_index:
                return [num_to_index[target - num], i]

            num_to_index[num] = i

        return []   # no sum

'''Example:
nums = [2, 7, 11, 15]
target = 9


Step by step:

1. Initialize an empty dictionary `num_to_index`.
2. Start iterating through the `nums` array using `enumerate()`:

- In the first iteration, `i = 0` and `num = 2`.
- Check if the difference between the `target` (9) and the current `num` (2) exists as a key in the `num_to_index`
dictionary. Since 9 - 2 = 7, 7 is not in the dictionary yet.
- Add `num` as a key to the `num_to_index` dictionary with its corresponding index `i` (0).

3. Move to the next iteration:

- In the second iteration, `i = 1` and `num = 7`.
- Check if the difference between the `target` (9) and the current `num` (7) exists as a key in the `num_to_index`
dictionary. Since 9 - 7 = 2, 2 is present in the dictionary.
- The pair of numbers that add up to the target has been found. Return the indices [0, 1] corresponding to 2 and 7.

The solution returns the indices [0, 1], indicating that the numbers at indices 0 and 1 in the `nums` array (2 and 7)
add up to the target value of 9.'''

