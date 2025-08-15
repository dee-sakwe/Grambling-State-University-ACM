"""
167. Two Sum II - Input Array Is Sorted (August 14, 2025)

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 3 * 104

-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000

The tests are generated such that there is exactly one solution.
"""

class Solution:
    from typing import List 

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Given an array of sorted nums and we have to find two that sum to target
        left, right = 0, len(numbers) - 1

        # If the pointers meet, the sum doesn't exist
        while left < right:
            # First check that the values sum to target
            total = numbers[left] + numbers[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]
            
        # If we get to this point, sum doesn't exist
        # Not strictly necessary for this question, but still good practice
        return 0
    
    # Algorithm runs in O(n) time and O(1) space

# Testing phase
test = Solution()

print(f"First test case: {test.twoSum([2,7,11,15], 9)} \n")  # Expected value: [1,2]
print(f"Second test case: {test.twoSum([2,3,4], 6)} \n")  # Expected value: [1,3]
print(f"Third test case: {test.twoSum([-1, 0], -1)} \n")  # Expected value: [1,2]
# Doesn't exist scenario
print(f"Fourth test case: {test.twoSum([2,7,11,15,24,25], 23)}")  # Expected value: 0
