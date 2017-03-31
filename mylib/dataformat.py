def objToMatrix(ls):
    result = []
    keys = ls[0].keys()


    for obj in ls:
        row = []
        for key in keys:
            value = obj[key]
            row = row + [value]
        result = result + [row]
    return  result

def matrixRotate(matrix):
    result = []
    h = len(matrix)
    w = len(matrix[0])
    for i in range(0,w-1):
        row = []
        for j in range(0,h-1):
            value = matrix[j][i]
            row = row + [value]
        result = result + [row]
    return result



