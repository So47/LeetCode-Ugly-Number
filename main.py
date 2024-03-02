class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive.
        if n <= 0:
            return False

        # Divide n by 2, 3, and 5 as long as possible.
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n = n // prime

        # If n has been reduced to 1, it is ugly.
        return n == 1
        
