# Making Change
`Algorithm`
`Python`

## Tasks
+ 0. **Change comes from within**

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: def makeChange(coins, total)
- Return: fewest number of coins needed to meet total
    - If total is 0 or less, return 0
    - If total cannot be met by any number of coins you have, return -1
- coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task
```
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
```

```
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```

*Solution explanation*
```
def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
```

This function uses **dynamic programming** to compute the fewest number of coins needed to meet the given total amount. It first checks for some edge cases: if total is 0 or less, it returns 0; if there are no coins that can add up to total, it returns -1.

Otherwise, it initializes an array dp of size total+1, where dp[i] will store the fewest number of coins needed to make the amount i. It sets dp[0] = 0, since it takes 0 coins to make an amount of 0.

Then, for each amount i from 1 to total, it tries to use each coin in coins to make that amount. If a coin coin is less than or equal to i, then it can be used to make the amount i, by adding 1 coin to the fewest number of coins needed to make the amount i-coin. So the function updates dp[i] to the minimum value of dp[i] and dp[i-coin]+1.

Finally, the function returns dp[total] if it's not equal to infinity (meaning there was a way to make the total amount), or -1 otherwise.

*However, dynamic programming is less efficient.*
The time complexity of the dynamic programming approach for the makeChange function is O(nm), where n is the size of the coins list and m is the total amount to make. This is because the function constructs a 2D table of size (n+1) x (m+1) to store the intermediate results.

The outer loop of the dynamic programming algorithm runs m times, while the inner loop runs n times for each value of m. The body of the inner loop has a constant time complexity of O(1) (since it's just doing simple arithmetic operations), so the overall time complexity is O(nm).

Instead of using a dynamic programming approach, we can use a **greedy algorithm** that always selects the largest coin possible at each step.

In [0-making_change.py](0-making_change.py) i've thus used the greedy algorithm. Here is the code explanation: 

This implementation first sorts the coins list in descending order, so that we always try to use the largest coin possible first. Then it initializes a counter count to 0.

For each coin in coins, the function repeatedly subtracts the coin value from the total amount as long as the coin value is less than or equal to the total. It also increments the count variable by 1 for each coin used. Once the total is less than the coin value, the function moves on to the next coin.

At the end, the function checks if the total is 0 (meaning we were able to make the total amount using some combination of coins), and returns the count variable if it is, or -1 otherwise.

This implementation has a time complexity of O(n log n), due to the sorting of the coins list. However, in practice, the list of coins is likely to be small, so the overhead of sorting should be negligible. The overall algorithm is still essentially linear in the size of the total amount, so it should be much faster than the dynamic programming approach for large values of total.
