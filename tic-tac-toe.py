import os
import random

matriz=[ [" "," "," "],
         [" "," "," "],
         [" "," "," "] ]
palavra=['L','I','N','H','A']

def msgError():
    print("Digite um valor válido!")
    input("Pressione ENTER")

def passaJogador(jogador):
    if jogador==1:
        return 2,'O'
    else:
        return 1,'X'

def desenhaMatriz():
    aux=0
    os.system("cls")
    print("\nJOGO DA VELHA\n")
    print("       COLUNA")
    print("      0   1   2")
    for i in range(0,3):
        for j in range (0,3):
            if j is not 0:
                print("|",end="")
            else:
                print(palavra[aux],"",i,end=" ")
                aux+=1
            print("",matriz[i][j],"",end="")
        if i is not 2:
            print("\n",end="")
            print(palavra[aux],"   ———|———|———")
            aux+=1
    print("\n")

#Inicia com o jogador 1
quemJoga=1
caracter='X'
while True:
    desenhaMatriz()
    print("Vez do jogador "+str(quemJoga)+"!")
    linha=input("Linha: ")
    coluna=input("Coluna: ")
    if (int(linha) or int(coluna))<0: msgError()
    else:
        try:
            matriz[int(linha)][int(coluna)]=caracter
            quemJoga,caracter=passaJogador(quemJoga)
        except:
            msgError()