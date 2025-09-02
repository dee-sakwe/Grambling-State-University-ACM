from typing import List


def strStr(haystack: str, needle: str) -> int:
    """
    Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.
    """
    right = 0
    n = len(needle)
    h = len(haystack)

    if n > h:
        return -1

    while right < len(haystack):
        if haystack[right] == needle[0]:
            matches = True

            if (right + n) > h:
                return -1

            for i in range(1, n):
                if haystack[right + i] != needle[i]:
                    matches = False

            if matches:
                return right

        right += 1

    return -1


def maxProfit(prices: List[int]) -> int:
    """
    You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    min_price, max_profit = float("inf"), 0

    for price in prices:
        if price < min_price:
            min_price = price

        else:
            max_profit = max(max_profit, (price - min_price))

    return max_profit


def majorityElement(nums: List[int]) -> int:
    """
    Given an array `nums` of size `n`, return the majority element.

    The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.
    """
    # freqs = {}
    # majority = 0

    # for num in nums:
    #     freqs[num] = freqs.get(num, 0) + 1

    #     if freqs[num] > freqs.get(majority, 0):
    #         majority = num

    # return majority
    
    # Boyer-Moore
    maj = nums[0]
    times = 0

    for num in nums:
        if times == 0:
            maj = num

        if num == maj:
            times += 1
        else:
            times -= 1

    return maj

class Logger:
    """
    Design a logger system that receive stream of messages along with its timestamps.

    A message should be printed if and only if it has not been printed in the last 10 seconds.

    In the method `couldPrintMessage()`, given a `message` and a `timestamp` in seconds, return `true` if the message can be printed within the given timestamp, otherwise return `false`.
    """

    def __init__(self) -> None:
        self.messages: dict[str, int] = {}

    def could_print_message(self, timestamp: int, message: str) -> bool:
        if message in self.messages:
            if timestamp - self.messages[message] >= 10:
                self.messages[message] = timestamp
                return True
            else:
                return False

        else:
            self.messages[message] = timestamp
            return True


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

    Each letter in `magazine` can only be used once in `ransomNote`.
    """
    from collections import Counter

    if len(ransomNote) > len(magazine):
        return False

    ransomCount = Counter(ransomNote)
    magazineCount = Counter(magazine)

    for letter in ransomNote:
        if ransomCount[letter] > magazineCount.get(letter, 0):
            return False

    return True

    # O(n) runtime O(n + m) space


def arrange_coins(n: int) -> int:
    """
    You have `n` coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

    Given the integer `n`, return the number of complete rows of the staircase you will build.
    """
    # O(N) solution

    # if n == 1:
    #     return 1

    # stairs = 0

    # for i in range(1, n):
    #     if i <= n:
    #         stairs += 1
    #         n -= i

    #     else:
    #         break

    # return stairs

    # Binary Search O(logn) solution
    # Initialize pointers to first and last possible row lengths
    left, right = 1, n
    
    while left <= right:
        # Compute the midpoint between left and right
        mid = left + (right - left) // 2
        
        # Compute the total number of coins needed for mid complete rows
        coins = (mid * (mid + 1)) // 2
        
        # If we have enough coins, look for a smaller number of rows
        if coins <= n:
            left = mid + 1
        # Otherwise, look for a larger number of rows
        else:
            right = mid - 1
            
    # Return the number of complete rows (i.e., right pointer)
    return right
