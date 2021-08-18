import os

matriz=[ [" "," "," "],
         [" "," "," "],
         [" "," "," "] ]

def desenhaMatriz():
    print("\n—————————————")
    for i in range(0,3):
        for j in range (0,3):
            print("|",matriz[i][j],"",end="")
        print("|\n—————————————")
    print("\n")

desenhaMatriz()