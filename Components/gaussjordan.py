import numpy as np

def gauss_jordan(matrix, sol_matrix):
    matrix = np.array(matrix, float)
    sol_matrix = np.array(sol_matrix, float)
    n = len(sol_matrix)
    
    for k in range(n):
        if np.fabs(matrix[k,k])< 1.0e-12:
            for i in range(k+1,n):
                if np.fabs(matrix[i,k]) > np.fabs(matrix[k,k]):
                    for j in range(k,n):
                        matrix[k,j], matrix[i,j] = matrix[i,j],matrix[k,j]
                    sol_matrix[k],sol_matrix[i] = sol_matrix[i],sol_matrix[k]
                    break
        pivot = matrix[k,k]
        for j in range(k,n):
            matrix[k,j] /= pivot
        sol_matrix[k] /= pivot
        
        for i in range(n):
            if i == k or matrix[i,k] == 0: continue
            factor = matrix[i,k]
            for j in range(k,n):
                matrix[i,j] -= factor * matrix[k,j]
            sol_matrix[i] -= factor*sol_matrix[k]
            
    return sol_matrix, matrix
*return [6.1538, 1.5385]*
