class Solution(object):
    def rotate(matrix):
        output_matrix = [[]]*len(matrix)
        # print("Output Matrix: ", output_matrix)
        # print(len(matrix))
        for i in range(0,len(matrix)):
            new = []
            # print("output_matrix[i]: ",output_matrix[i])
            for j in range(len(matrix)-1,-1,-1):
                new.append(matrix[j][i])
            output_matrix[i] = new
        matrix = output_matrix
        print("Final: ",matrix)
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
Solution.rotate(matrix1)