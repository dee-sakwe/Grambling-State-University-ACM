from typing import List

print("Chapter 1: Two Pointers")

# Understand Match Plan Implement Review Evaluate?

"""
Given an array of integers, return all triplets (a, b, c] such that a + b + c = 0. The
solution must not contain duplicate triplets (e.g., [ 1, 2, 3] and [ 2, 3, 1] are considered
duplicate triplets), If no sud! triptets are found, return an empty array.
Each triplet can be arranged in any order:, and the output can be returned in any order.

.Example

Input nuin.s = (0, -1" 2, -3, 1)
Output [(-3, 1, 2], [-1, 0, ll]
"""


def twoSum(numbers: List[int], target: int) -> List[int]:
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
            return [left, right]

    # If we get to this point, sum doesn't exist
    # Not strictly necessary for this question, but still good practice
    return []

    # Algorithm runs in O(n) time and O(1) space


def triplet_sum(nums: List[int]) -> List[List[int]]:
    # Sort the input array and fix each element and then use the twoSum function to find the rest
    working_array = sorted(nums)
    working_length = len(working_array) - 2

    result: List[list] = []

    for i in range(working_length):
        if i > 0 and working_array[i] == working_array[i - 1]:
            continue

        temp = working_array[i + 1 :]
        others = twoSum(temp, -(working_array[i]))

        if others:
            first, second = others
            result.append([working_array[i], temp[first], temp[second]])

    return result

    print(triplet_sum([0, -1, 2, -3, 1]))


def is_valid_palindrome(s: str) -> bool:
    """
    A palindrome Is a sequence of characters that reads the same forward and backward.
    Given a strin,g. determine if it's a palindrome after removing all non-alphanumeric characters. A character is alphanumeric if it's either a letter or a number.

    Constraints:
    The string may include a combination of lowercase English letters, numbers, spaces, and
    punctuations.
    """
    left, right = 0, len(s) - 1

    while left < right:
        while not s[left].isalpha():
            left += 1

        while not s[right].isalpha():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

    print(is_valid_palindrome("a dog! a panic in a pagoda."))  # Expected: True


def largest_container(heights: List[int]) -> int:
    """
    You are given an array of numbers, each representing the height of a vertical line on a graph,
    A container can be formed with any pair of these lines, along with the x-axis of the graph,
    Return the amount of water which the largest container can hold.
    """

    # Take a greedy approach
    left, right = 0, len(heights) - 1

    # The max we currently have is the widest container
    max_amount = min(heights[left], heights[right]) * (right - left)

    while left < right:
        # Calculate the amount of water the container can hold
        amount = min(heights[left], heights[right]) * (right - left)

        # Update max amount if the calculated amount is larger
        max_amount = max(max_amount, amount)

        # To know which pointer to move, we have to check which of heights[left]
        # and heights[right] is bigger

        if heights[right] < heights[left]:
            right -= 1

        else:
            left += 1

    return max_amount

    print(largest_container([2, 7, 8, 3, 7, 6]))


def move_zeros(nums: List[int]) -> List[int]:
    """
    Given an array of integers, modify the array in place to move all zeros to the end while
    maintaining the relative order of non-zero elements.
    Example:
    Input: nums = [0, 1, 0, 3, 2]
    Output: [1, 3, 2, 0, 0]
    """

    # unidirectional traversal?
    left, right = 0, 1
    n = len(nums)

    while right < (n - 1):
        while nums[left] != 0:
            left += 1

        while nums[right] == 0:
            right += 1

        nums[left], nums[right] = nums[right], nums[left]

    return nums

    print(move_zeros([0, 1, 0, 1, 0, 3, 0, 2, 0, 0, 2, 3, 0, 3, 0, 0, 5]))


def next_lexicographical_sequence(s: str) -> str:
    # Turn the string to a list of individual characters I can work with
    letters = list(s)

    # Traverse from right to left to find pivot
    left = len(s) - 1
    right = len(s) - 1

    pivot = ""

    while left > 0:
        if letters[left - 1] < letters[left]:
            pivot = letters[left - 1]
            break

        left -= 1

    # If no pivot (non_decreasing), return s reversed
    if not pivot:
        return "".join(letters[::-1])

    # swap pivot with char larger than it on the right
    # we can traverse the string from the right till we find
    # a char bigger than the pivot
    while right > 0:
        if letters[right] > pivot:
            letters[left - 1], letters[right] = letters[right], letters[left - 1]
            break

        right -= 1

    # make the substring after the pivot as small as possible (reverse it)
    letters = letters[:left] + letters[left:][::-1]

    return "".join(letters)

    print(next_lexicographical_sequence("ynitsed"))
