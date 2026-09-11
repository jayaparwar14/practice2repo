class solution :

    def Rotate90deg1 (self,matrix,) :

        n = len(matrix)
        result = [[0 for _ in range (n)] for _ in range (n)] 

        for i in range (0,n) :
            
            for j in range (0,n) :

                result[j][n - 1 -i] = matrix[i][j]

        return result
    

    def PrintRes (self,result) :

        n = len(result)

        for i in range (0,n) :

            for j in range (0,n) :

                print(result[i][j],end = " ")

            print()


    def Rotate90deg2 (self,matrix) :

        n = len(matrix) 

        for i in range (0,n-1) :

            for j in range (i+1,n) :

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

                
        for i in range (0,n) :

            matrix[i].reverse()

        n = len(matrix)

        for i in range (0,n) :

            for j in range (0,n) :

                print(matrix[i][j],end = " ")

            print()

        
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range (0,4) :

    for j in range (0,4) :

        print(matrix[i][j],end = " ")

    print()

S = solution()
# Rotated = S.Rotate90deg1(matrix)

# print("Matrix after rotate 90 degree :")
# S.PrintRes(Rotated)

print("Matrix after rotate 90 degree :")
S.Rotate90deg2(matrix)


