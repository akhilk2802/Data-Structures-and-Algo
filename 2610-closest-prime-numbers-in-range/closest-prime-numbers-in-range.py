class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        primeNumbers = []

        def isPrime(n):
            if n < 2:
                return False
            if n in (2, 3):
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False

            for i in range(5, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True

        for number in range(left, right + 1):
            if isPrime(number):
                primeNumbers.append(number)

        print("primeNumbers : ", primeNumbers)
        minVal = float("inf")
        a, b = -1, -1

        for i in range(1, len(primeNumbers)):
            val = primeNumbers[i] - primeNumbers[i-1]

            if val < minVal:
                minVal = val
                a = primeNumbers[i-1]
                b = primeNumbers[i]


        return [a, b]

                

