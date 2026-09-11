class solution :

    def SpiralMatrix (self,matrix) :

        top , left = 0,0
        bottom , right = len(matrix) - 1 , len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right :

            for i in range (left , right + 1) :

                result.append(matrix[top][i])
            top += 1

            for i in range (top , bottom + 1) :

                result.append(matrix[i][right]) 
            right -= 1

            if top <= bottom :

                for i in range (right , left - 1 , -1) :

                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right :

                for i in range (bottom ,top - 1 , -1) :

                    result.append(matrix[i][left]) 
                left += 1

        return result 
        
    def print (self,result) :
                
            for val in result :
                    
                print(val,end = " ")

            print()



matrix = [[1,2,3,4,5,6],[20,21,23,24,25,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]
S = solution() 
# spiral = S.SpiralMatrix(matrix)
# S.print(spiral)

print(S.SpiralMatrix(matrix))

