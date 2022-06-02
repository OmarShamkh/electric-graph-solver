# Electric Graph Solver
Console application to calculate Cut-set and Tie-set Matrices Realted to Computer-aided-design.

## Overview:
Any electric circuit or network can be converted into its equivalent graph by replacing
the passive elements and voltage sources with short circuits and the current sources
with open circuits.
Ex:
![cad-sc](https://user-images.githubusercontent.com/44472968/171685320-88889a9e-584e-4fdb-a0d8-9ef676599b87.png)


## How it works:
* Give Incidence Matrix(A) as an input.Calculate Cut-set(C) Matrix and Tie-set(B) Matrix.
* The value of element will be +1 for the link of selected f-loop.
* The value of elements will be 0 for the remaining links and branches, which are not part of
the selected f-loop.
* If the direction of branch current of selected f-loop is same as that of f-loop link current, then
the value of element will be +1.
* If the direction of branch current of selected f-loop is opposite to that of f-loop link current,
then the value of element will be -1.

![Cad-example](https://user-images.githubusercontent.com/44472968/171685638-a539ac58-8c6b-4bfb-9b43-b8c6d335c0ad.png)


## Build:
```bash
git clone https://github.com/OmarShamkh/network-graphs-solver.git
python3 main.py
```

## Snapshot:
![cad-demo](https://user-images.githubusercontent.com/44472968/171695844-7b51d529-d425-43d7-9b81-9ec595c74430.gif)
