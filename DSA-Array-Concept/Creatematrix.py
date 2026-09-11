class solution :

    def CreateMatrix (self,nums) :

        rows = len(nums) 
        cols = len(nums[0])

        for i in range (0,rows) :

            for j in range (0,cols) :

                print(nums[i][j],end = " ")

            print()

    def printUpperTri (self,nums) :

        rows = len(nums) 
        cols = len(nums[0])

        print("The lower triangle of matrix is")


        for i in range (0,rows) :

            for j in range (0,cols) :

                if (j >= i) :

                    print(nums[i][j],end = " ")
                
                else :

                    print("*",end = " ")

            print()

    def printLowerTri (self,nums) :

        rows = len(nums) 
        cols = len(nums[0])

        print("The lower triangle of matrix is")

        for i in range (0,rows) :

            for j in range (0,cols) :

                if (j <= i) :

                    print(nums[i][j],end = " ")
                
                else :

                    print("*",end = " ")

            print()

    def printdiagonal1 (self,nums) :

        rows = len(nums) 
        cols = len(nums[0])

        print("The diagonal of matrix is")

        for i in range (0,rows) :

            for j in range (0,cols) :

                if (j == i) :

                    print(nums[i][j],end = " ")
                
                else :

                    print("*",end = " ")

            print()

    def printdiagonal2 (self,nums) :

        rows = len(nums) 
        cols = len(nums[0])

        print("The diagonal of matrix is")

        for i in range (0,rows) :

            for j in range (0,cols) :

                if (j == cols - i - 1) :

                    print(nums[i][j],end = " ")
                
                else :

                    print("*",end = " ")

            print()

    def transpos (self,nums) :

        rows = len(nums) 
        cols = len(nums[0])
        res = [[0] * rows for _ in range (cols)]

        for i in range (0,rows) :

            for j in range (0,cols) :

                res[j][i] = nums[i][j]
        
        for i in range (0,rows) :

            for j in range (0,cols) :

                print(res[i][j],end = " ")

            print()
                
            


nums = [[1,2,3],[4,5,6],[7,8,9]]
S = solution()
S.printdiagonal2(nums)