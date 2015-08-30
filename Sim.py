from __future__ import division

def genMatrix(rows,cols):
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            print matrix[i][j],
        print '\n'

def SimScore(fp1, fp2):
    len1 = len(fp1) + 1
    len2 = len(fp2) + 1
    matrix = [[0 for col in range(len2)] for row in range(len1)]
    cost = 1
    for row in range(len1):
        for col in range(len2):
            if row == 0 or col == 0:
                continue

            if(fp1[row-1] == fp2[col-1]):
                cost = 0
            else:
                cost = 1

            matrix[row][col] = min(matrix[row-1][col]+1, matrix[row][col-1]+1,matrix[row-1][col-1]+cost)

    #for i in range(len1):
    #    for j in range(len2):
    #        print matrix[i][j],
    #   print '\n'

    sim_score = matrix[len1-1][len2-1] / max(len1-1, len2-1)
    sim_score = 1 - sim_score
    sim_score *= 100
    return sim_score
