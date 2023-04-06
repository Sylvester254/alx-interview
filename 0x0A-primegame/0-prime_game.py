#!/usr/bin/python3
def isWinner(x, nums):
    """
    Helper function to get all primes up to a given number
    """
    def getPrimes(n):
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return [i for i in range(n+1) if sieve[i]]

    """
    Helper function to check if there are any primes left in the list
    """
    def hasPrimes(lst):
        for num in lst:
            if num != 0 and num != 1 and all(num % i != 0
                                             for i in range
                                             (2, int(num**0.5)+1)):
                return True
        return False

    """
    Helper function to simulate a round of the game
    """
    def playRound(lst, player):
        primes = getPrimes(lst[-1])
        for prime in primes:
            if prime in lst:
                for i in range(prime, lst[-1]+1, prime):
                    if lst[-i] != 0:
                        lst[-i] = 0
                if not hasPrimes(lst):
                    return player
        return None

    """
    Main function to play x rounds of the game
    """
    winner_counts = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        lst = [j for j in range(0, nums[i]+1)]
        winner = None
        while winner is None:
            winner = playRound(lst, 'Maria')
            if winner is None:
                winner = playRound(lst, 'Ben')
        winner_counts[winner] += 1

    """
    Determine the winner based on who won the most rounds
    """
    if winner_counts['Maria'] > winner_counts['Ben']:
        return 'Maria'
    elif winner_counts['Ben'] > winner_counts['Maria']:
        return 'Ben'
    else:
        return None
