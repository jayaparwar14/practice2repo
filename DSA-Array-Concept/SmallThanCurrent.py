class solution :
    
    def SmallThanCurrent (self,nums) :
        self.ans = []

        for i in nums :
            c = 0
            for j in nums :

                if (j < i) :
                    c += 1

            self.ans.append (c)

        return self.ans
    
    def show (self) :
        print (self.ans)
    
nums = [8,1,2,2,3]
    
S = solution()
S.SmallThanCurrent(nums)
S.show()

class solution2 :

    def countdigits (self,nums) :
        temp = nums
        ans = 0

        while temp > 0 :

            r = temp % 10 
            if (nums % r == 0) :
                ans += 1
            
            temp //= 10
        
        print(ans)

        return ans
    
    

nums = 123456
D = solution2()
D.countdigits(nums)
