from typing import List


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
    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2

        coins = mid * (mid + 1) // 2

        if coins == n:
            return mid
        elif coins < n:
            left = mid + 1
        elif coins > n:
            right = mid - 1

    return right
