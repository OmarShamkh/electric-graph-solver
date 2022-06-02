from Equations import Equations
solver = Equations()

class Outputs:

    # display matrix B and C 
    def Display(self):
        print("================================")
        print("Cut-set matrix C:")
        print(solver.CalcC())
        print("================================")
        print("Tie-set matrix B:")
        print(solver.CalcB())
        print("================================")

    
    