class solution :

    def fizzbuzz (self,n) :
        self.ans = []

        for i in range(1,n + 1):

            if (i % 3 == 0 and i % 5 == 0) :
                self.ans.append ("FizzBuzz")

            elif (i % 3 == 0) :
                self.ans.append ("Fizz")
            
            elif (i % 5 == 0) :
                self.ans.append ("Buzz")

            else :
                self.ans.append (i)

        return self.ans
        
    def show (self) :

        # for i in self.ans :
        #     print(i)
        print(self.ans)



S = solution()
S.fizzbuzz(15)
S.show()
