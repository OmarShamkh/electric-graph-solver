import numpy as np

# Enter Inputs
numberOfrows = int(input("Enter number of rows : "))
numberOfcols = int(input("Enter number of columns : "))

print("Enter Incidence matrix A:")
matrixA = []
for r in range(numberOfrows):
    col = list(map(int, input().split()))
    matrixA.append(col)

# Check if need extra row
flag = 0
for c in range(numberOfcols):
    posOne = 0
    negOne = 0
    for r in range(numberOfrows):
        posOne += matrixA[r][c] == 1
        negOne += matrixA[r][c] == -1
    flag |= (posOne != negOne)

# calculate the missing rows
if(flag):
    missed = []
    for c in range(numberOfcols):
        sum = 0
        for r in range(numberOfrows):
            sum += matrixA[r][c]
        if(sum > 0):
            missed.append(-1)
        elif(sum == 0):
            missed.append(0)
        else:
            missed.append(1)

    matrixA.append(missed)
    numberOfrows += 1

# calculate tree branches and links
TreeBranches = []
TreeLinks = []
maxRow = 0
ma = 0
nodes = numberOfrows
branches = numberOfcols  # 6
links = branches - nodes + 1
n = min(nodes, branches-links)
tree = nodes - 1  # 3

for r in range(numberOfrows):
    coutnNonZero = 0
    for c in range(numberOfcols):
        coutnNonZero += (matrixA[r][c] != 0)
    if(coutnNonZero > ma):
        ma = coutnNonZero
        maxRow = r  # --> node which has the greatest number of branches in

# Tree Branches
ones = 0
negOnes = 0
for c in range(numberOfcols):
    ones += matrixA[maxRow][c] == 1
    negOnes += matrixA[maxRow][c] == -1

if(ones > negOnes):
    maxOnes = 1
else:
    maxOnes = -1

# Drive Tree branches and links
for c in range(numberOfcols):
    if(matrixA[maxRow][c] == maxOnes) and len(TreeBranches) < tree:
        TreeBranches.append(c)
    else:
        TreeLinks.append(c)

if(flag):
    numberOfrows -= 1

# calculate AT matrix
matrixAT = []
for i in range(numberOfrows):
    a = []
    for j in TreeBranches:
        a.append(matrixA[i][j])
    matrixAT.append(a)

# calculate AL matrix
matrixAL = []
for i in range(numberOfrows):
    a = []
    for j in TreeLinks:
        a.append(matrixA[i][j])
    matrixAL.append(a)

# calc Inverse of AT --> AT^-1
AT = np.array(matrixAT)
InvOfAT = np.linalg.inv(AT)

t1 = np.shape(InvOfAT)
t2 = np.shape(matrixAL)
# calculate matrix C link CL = AT^-1 * AL
matrixCL = np.dot(InvOfAT, matrixAL)

# Drive CT matrix -->  Identity matrix
matrixCT = []
n = numberOfrows
for i in range(n):
    a = []
    for j in range(n):
        if(i == j):
            a.append(1)
        else:
            a.append(0)
    matrixCT.append(a)


# calculate matrix C -->  C = CT + CL
matrixC = np.concatenate((matrixCT, matrixCL), axis=1)

# Drive matrix BT  = -1 * CL transpose
matrixBT = np.transpose(matrixCL)

l = (len(matrixBT))
for i in range(l):
    for j in range(len(matrixBT[i])):
        if(matrixBT[i][j] != 0):
            matrixBT[i][j] = -matrixBT[i][j]


# matrixBL --> identity matrix
matrixBL = []
for i in range(len(matrixBT)):
    a = []
    for j in range(len(matrixBT)):
        if(i == j):
            a.append(1)
        else:
            a.append(0)
    matrixBL.append(a)


# calculate matrix B = BT + BL
matrixB = np.concatenate((matrixBT, matrixBL), axis=1)

print("================================")
print("Answer:")
print("Cut-set matrix C:")
print(matrixC)
print("================================")
print("Tie-set matrix B:")
print(matrixB)

# test cases:
# 3 * 6
# 1 0 1 0 0 -1
# 0 1 -1 0 1 1
# 0 0 0 1 -1 0

# 3 * 5
# -1 1 1 1 0
# 0 0 0 -1 0
# 1 -1 0 0 -1
