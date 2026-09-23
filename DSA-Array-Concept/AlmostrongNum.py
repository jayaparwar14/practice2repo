class Solution :

    def IsPalindrome (slef,n) :

        nums = n
        result = 0 

        while nums > 0 :

            ld = nums % 10
            result = (result * 10) + ld 
            nums = nums // 10

        return n == result 

    def AlmostrongNumber (self,n) :

        nums = n
        total = 0
        strength = len(str(n))

        while nums > 0 :

            ld = nums % 10
            total = total + (ld ** strength) 
            nums = nums // 10

        return total == total


n = 4638
S = Solution()
print(S.AlmostrongNumber(n))