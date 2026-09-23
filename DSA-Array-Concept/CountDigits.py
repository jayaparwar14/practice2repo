import math

class Solution :

    def CountDigits1(slef,n) :

        num = n
        count = 0

        while num > 0 :

            count += 1
            num = num // 10

        return count

    def  CountDigits2 (slef,n) : 

        return int(math.log10(n) + 1)


n = 5438
S = Solution()
print(S.CountDigits2(n))