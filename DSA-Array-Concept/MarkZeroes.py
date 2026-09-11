class solution :

    def MarkInfinity (self,matrix,row,cols) :

        r = len(matrix)
        c = len(matrix[0])

        for i in range (0,r) :

            if (matrix[i][cols] != 0) :
                
                matrix[i][cols] = float("inf")

        for i in range (0,c) :

            if (matrix[row][i] != 0) :

                matrix[row][i] = float("inf")

    def SetZeroes1 (self,matrix) :

        r = len(matrix) 
        c = len(matrix[0])

        for i in range (0,r) :

            for j in range (0,c) :

                if (matrix[i][j] == 0) :

                    self.MarkInfinity(matrix,i,j) 

        for i in range (0,r) :

            for j in range (0,c) :

                if (matrix[i][j] == float("inf")) :

                    matrix[i][j] = 0

        for i in range (0,r) :

            for j in range (0,c) :

                print(matrix[i][j],end = " ")

            print()


    def SetZeroes2 (self,matrix) :

        r = len(matrix)
        c = len(matrix[0])
        rowTrack = [0 for _ in range(r)]
        colTrack = [0 for _ in range(c)]


        for i in range (0,r) :

            for j in range (0,c) :

                if (matrix[i][j] == 0) :

                    rowTrack[i] = -1
                    colTrack[j] = -1

        for i in range (0,r) :

            for j in range (0,c) :

                if (rowTrack[i] == -1 or colTrack[j] == -1) :

                    matrix[i][j] = 0

        for i in range (0,r) :

            for j in range (0,c) :

                print(matrix[i][j],end = " ")

            print()



matrix = [[1,2,3,4],[5,0,0,6],[7,8,9,2]]

for i in range (0,3) :

    for j in range (0,4) :

        print(matrix[i][j],end = " ")

    print()

S = solution()
print("Matrix after set zero :")
S.SetZeroes2(matrix)