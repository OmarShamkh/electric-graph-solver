from inputs import Inputs
import numpy as np
input = Inputs()

TreeBranches = []
TreeLinks = []
class Equations:

    def __init__(self):
        self.flag = 0
        self.numberOfrows = input.getnumberOfrows()
        self.numberOfcols = input.getnumberOfcols()
        self.matrixA = input.getmatrixA()
        self.matrixCL = []

        
    def CheckExtraRows(self):
        for c in range(self.numberOfcols):
            posOne = 0
            negOne = 0
            for r in range(self.numberOfrows):
                posOne += self.matrixA[r][c] == 1
                negOne += self.matrixA[r][c] == -1
            self.flag |= (posOne != negOne)

        if(self.flag):
            missed = []
            for c in range(self.numberOfcols):
                sum = 0
                for r in range(self.numberOfrows):
                    sum += self.matrixA[r][c]
                if(sum > 0):
                    missed.append(-1)
                elif(sum == 0):
                    missed.append(0)
                else:
                    missed.append(1)

            self.matrixA.append(missed)
            self.numberOfrows += 1

    
    # node which has the greatest number of branches -->in/out
    def CalcNode(self):
        self.CheckExtraRows()
        maxRow = 0
        ma = 0
        for r in range(self.numberOfrows):
            coutnNonZero = 0
            for c in range(self.numberOfcols):
                coutnNonZero += (self.matrixA[r][c] != 0)
            if(coutnNonZero > ma):
                ma = coutnNonZero
                maxRow = r
        return maxRow

    def CalcTreeBranchesAndLinks(self):
        MaxNode = self.CalcNode()
        self.nodes = self.numberOfrows
        self.branches = self.numberOfcols
        self.links = self.branches - self.nodes + 1
        self.tree = self.nodes - 1
        ones = 0
        negOnes = 0
        for c in range(self.numberOfcols):
            ones += self.matrixA[MaxNode][c] == 1
            negOnes += self.matrixA[MaxNode][c] == -1
        if(ones > negOnes):
            maxOnes = 1
        else:
            maxOnes = -1
        for c in range(self.numberOfcols):
            if(self.matrixA[MaxNode][c] == maxOnes) and len(TreeBranches) < self.tree:
                TreeBranches.append(c)
            else:
                TreeLinks.append(c)


    # calculate AT matrix
    def CalcAT(self):
        AT = []
        for r in range(self.numberOfrows):
            row = []
            for c in TreeBranches:
                row.append(self.matrixA[r][c])
                # print(r, c)
            AT.append(row)
        return AT

    # calc Inverse of AT --> AT^-1
    def CalcATInverse(self):
        return np.linalg.inv(np.array(self.CalcAT()))

    # calculate AL matrix
    def CalcAL(self):
        AL = []
        for r in range(self.numberOfrows):
            row = []
            for c in TreeLinks:
                row.append(self.matrixA[r][c])
            AL.append(row)
        return AL

    # calculate matrix C link CL = AT^-1 * AL
    def CalcCL(self):
        return np.dot(self.CalcATInverse(), self.CalcAL())

    # Drive CT matrix -->  Identity matrix
    def CalcCT(self):
        matrixCT = []
        n = self.numberOfrows
        for i in range(n):
            a = []
            for j in range(n):
                if(i == j):
                    a.append(1)
                else:
                    a.append(0)
            matrixCT.append(a)
        return matrixCT


    # calculate matrix C -->  C = CT + CL
    def CalcC(self):
        self.CalcTreeBranchesAndLinks()
        if(self.flag):
            self.numberOfrows -= 1
        self.matrixCL = self.CalcCL()
        return np.concatenate((self.CalcCT(), self.matrixCL) , axis=1)

    # calculate matrix B = BT + BL
    def CalcB(self):
        self.matrixBT = np.transpose(self.matrixCL)
        l = (len(self.matrixBT))
        for i in range(l):
            for j in range(len(self.matrixBT[i])):
                if(self.matrixBT[i][j] != 0):
                    self.matrixBT[i][j] = -1 * self.matrixBT[i][j]

        # matrixBL --> identity matrix
        self.matrixBL = []
        for i in range(len(self.matrixBT)):
            a = []
            for j in range(len(self.matrixBT)):
                if(i == j):
                    a.append(1)
                else:
                    a.append(0)
            self.matrixBL.append(a)
        return np.concatenate((self.matrixBT, self.matrixBL), axis=1)
