from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.



    Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
    Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]


    Constraints:

    - 2 <= nums.length <= 104
    - -109 <= nums[i] <= 109
    - -109 <= target <= 109
    - Only one valid answer exists.
    """

    # Create a hashmap to keep track of numbers we've already seen in nums
    others: dict[int, int] = {}

    for i in range(len(nums)):
        curr = nums[i]

        if (target - curr) in others:
            return [others[target - curr], i]

        others[nums[i]] = i

    return []


    print(two_sum([3, 3, 6, 1, 2, 4, 5, 8, 10], 10))


def isPalindrome(x: int) -> bool:
    """
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:

        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:

        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:

        Input: x = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    

    Constraints:

    - `-2^31 <= x <= 2^31 - 1`
    

    Follow up: Could you solve it without converting the integer to a string?
    """
    if x < 0:
        return False

    # I think something to do with modulo 10 can help with this
    reverse: List[int] = []

    working = x

    while working > 0:
        # Reconstruct the number from the back
        last_digit = working % 10
        # use integer division to have our next working
        working = working // 10
        # append last_digit to reverse
        reverse.append(last_digit)

    # After our while loop finishes running, we reconstruct the number
    n = len(reverse) - 1
    power = n
    rev_num: int = 0

    while power >= 0:
        rev_num += reverse[n - power] * (10 ** power)
        power -= 1

    return x == rev_num

    print(isPalindrome(2010102))


def longestCommonPrefix(self, strs: List[str]) -> str:
    # Empty strs edge case
    if not strs:
        return ""

    result: List[str] = []
    # The longest common prefix is limited by the shortest word
    shortest_word = min(strs)

    for i in range(len(shortest_word)):
        letter = shortest_word[i]

        for word in strs:
            if word[i] != letter:
                return "".join(result)

        result.append(letter)

    return "".join(result)

    # O(n * m) time where n = len(strs[0]) and m = len(strs)


def removeElement(nums: List[int], val: int) -> int:
    """
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    """
    # Two-pointers
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] == val:
            right += 1
        
        else:
            nums[left] = nums[right]
            left += 1
            right += 1

    nums = nums[:left+1]

    return left

