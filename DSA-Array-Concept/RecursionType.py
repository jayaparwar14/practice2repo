class Solution :

    # Parameterized Recursion 

    def Sum (self , add , i , n) :

        if i > n :

            return add

        return self.Sum (add + i , i + 1 , 4)


    # Functional Recursion 
    
    def Factorial (self , N) :

        if N == 1 :

            return 1

        return N * self.Factorial (N - 1)


    def Factorial (self , N) :

        if N == 1 :

            return 1

        return N * self.Factorial (N - 1)

    def ReverseArray (self, nums , left , right) :

        if left > right : 

            return nums

        nums[left] , nums[right] = nums[right] , nums[left]
        

        return self.ReverseArray (nums , left + 1 , right - 1)

   
nums = [31,94,36,23,1,2,3,4,5,45,89,52,61]
S = Solution()
print(S.Sum (0 , 1 , 4))
print(S.Factorial(4))
print(S.ReverseArray(nums,4,8))
# rev = S.ReverseArray(nums , 0 , 4)
# print(rev)
