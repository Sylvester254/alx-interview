#!/usr/bin/python3
"""
The isWinner function takes in two arguments, x and nums.
x is the number of rounds, and nums is a list of integers
representing the values of n for each round.
The function returns the name of the player that won the
most rounds, or None if the winner cannot be determined.
"""


def isWinner(x, nums):
    """
    isWinner function takes in two arguments, x and nums
    and returns the name of the player that won the
    most rounds, or None
    """
    def is_prime(n):
        """
        Helper function is_prime checks whether a given
        number n is prime or not.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Helper function get_primes generates a list of
        prime numbers from 2 up to n
        """
        primes = []
        for i in range(2, n+1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(primes, n, is_maria_turn):
        """
        Helper function can_win checks whether the player
        whose turn it is can win the game, given the set
        of prime numbers and the current value of n.
        """
        if n == 1:
            return False

        has_moves = False
        for p in primes:
            if n % p == 0:
                if can_win(primes, n//p, not is_maria_turn):
                    return not is_maria_turn
                has_moves = True

        return has_moves

    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        primes = get_primes(nums[i])
        if can_win(primes, nums[i], True):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
