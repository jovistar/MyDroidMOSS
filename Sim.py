
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

            matrix[row][col] = min(matrix[row-1][col]+1, matrix[row][col-1]+1,
                                   matrix[row-1][col-1]+cost)

    #for i in range(len1):
    #    for j in range(len2):
    #        print matrix[i][j],
    #   print '\n'

    sim_score = matrix[len1-1][len2-1] / max(len1-1, len2-1)
    sim_score = 1 - sim_score
    sim_score *= 100
    return sim_score

#O(len(str2))空间复杂度，计算编辑距离
def CalDistance(str1, str2):
	matrix = []
	i = 0
	len1 = len(str1)
	len2 = len(str2)
	while i < (len2+1):
		matrix.append(i)
		i++
	i = 0
	while i < len1:
		tmp_i = matrix[0]
		matrix[0] += 1
		j = 0
		while j < len2:
			tmp_j = matrix[j+1]
			if str1[i] == str2[j]:
				matrix[j+1] = tmp_j
			else:
				matrix[j+1] = min(matrix[j],min(tmp_i,tmp_j))+1

	sim_score = matrix[len2] / max(len1, len2)
	sim_score = 1- sim_score
	sim_score *= 100
	return sim_score

