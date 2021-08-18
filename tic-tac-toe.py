import os
import random

matriz=[ [" "," "," "],
         [" "," "," "],
         [" "," "," "] ]

def desenhaMatriz():
    os.system("cls")
    print("\nJOGO DA VELHA\n")
    for i in range(0,3):
        for j in range (0,3):
            if j is not 0:
                print("|",end="")
            print("",matriz[i][j],"",end="")
        if i is not 2: print("\n———|———|———")
    print("\n")

desenhaMatriz()