class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        '''
        brute force solution -> 
        divide and convert it to string 
        return the val 
        '''

        if numerator == 0:
            return "0"

        result = []

        if numerator * denominator < 0:
            result.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        seen = {}

        while remainder:
            if remainder in seen:
                result.insert(seen[remainder], "(")
                result.append(")")
                break
            
            seen[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)