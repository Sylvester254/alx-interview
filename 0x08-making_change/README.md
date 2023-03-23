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

*Code explanation*
This function uses dynamic programming to compute the fewest number of coins needed to meet the given total amount. It first checks for some edge cases: if total is 0 or less, it returns 0; if there are no coins that can add up to total, it returns -1.

Otherwise, it initializes an array dp of size total+1, where dp[i] will store the fewest number of coins needed to make the amount i. It sets dp[0] = 0, since it takes 0 coins to make an amount of 0.

Then, for each amount i from 1 to total, it tries to use each coin in coins to make that amount. If a coin coin is less than or equal to i, then it can be used to make the amount i, by adding 1 coin to the fewest number of coins needed to make the amount i-coin. So the function updates dp[i] to the minimum value of dp[i] and dp[i-coin]+1.

Finally, the function returns dp[total] if it's not equal to infinity (meaning there was a way to make the total amount), or -1 otherwise.