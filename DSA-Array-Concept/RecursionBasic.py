class Solution :

    count = 0

    # Without Parameter

    # Head Recursion

    def func (self) :

        global count

        if self.count == 5 :
            return

        print("Jaya Parwar")
        self.count += 1

        self.func()

    # Tail Recursion 

    def func2 (self) :

        global count 

        if self.count == 5 :
            return 
        
        self.count += 1

        self.func()

        print("Jaya Parwar")

    # With Parameter

    # Head Recursion

    def greet1 (self,x,n) :

        if n == 0 :
            return 

        print(x)

        self.greet(x,n-1) 

    # Tail Recursion

    def greet2 (self,x,n) :
    
            if n == 0 :
                return 

            self.greet2(x,n-1) 
    
            print(x)

    # Head Recursion

    def Number1 (self,i,n) :

        if i > n :
            return 

        print(i)

        self.Number1(i + 1,n)

   

    def Number2 (self,n) :

        if n == 0 :
            return 

        print(n)

        self.Number2 (n-1)

    # Tail Recursion
    
    def Number3 (self,i,n) :
    
        if i > n :
            return 

        self.Number3 (i + 1,n)
    
        print(i)

    
    def Number4 (self,n) :

        if n == 0 :
            return 

        self.Number4 (n-1)

        print(n)

        
    
        
            
S = Solution()
# S.func2()
# S.greet2("Jayuu",5)
S.Number1(1,5)
S.Number2(5)
S.Number3(1,5)
S.Number4(5)
