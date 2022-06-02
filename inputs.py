
class Inputs:
    def __init__(self):
        self.rows = int(input("Enter number of rows : "))
        self.cols = int(input("Enter number of columns : "))
        
    def getnumberOfrows(self):
        return self.rows

    def getnumberOfcols(self):
        return self.cols

    def getmatrixA(self):
        print("Enter Incidence matrix A, **That contains 0,1,-1 ONLY!** ")
        matrixA = []
        for r in range(self.rows):
            row = list(map(int, input().split()))
            matrixA.append(row)
        return matrixA
