import math 

class Solution :

    def FactorGivenNum1 (self,num) :

        result = []

        for i in range (1,num + 1) :

            if (num % i == 0 ) :

                result.append(i)

        return result

    def FactorGivenNum2 (self,num) :

        result = []

        for i in range (1 , (num // 2) + 1) :

            if (num % i == 0) :

                result.append(i)

        result .append(num)

        return result

    def FactorGivenNum3 (self,num) :
    
        result = []
    
        for i in range (1 , int (math.sqrt(num)) + 1) :
    
            if (num % i == 0) :
    
                result.append(i)

            if ((num // i) != i ) :

                result.append(num // i)
    
        result.sort()
    
        return result


num = 10
S = Solution()
print(S.FactorGivenNum3(num))