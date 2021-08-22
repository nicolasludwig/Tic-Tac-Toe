import os
import random

palavra=['L','I','N','H','A']

def geraMatriz():
    return [[" "]*3 for _ in range(3)]

def msgError():
    print("Digite um valor válido!")
    input("Pressione ENTER")

def msgError2():
    print("Posição já preenchida!")
    input("Pressione ENTER")

def passaJogador(jogador):
    global countJogadas
    if jogador==1:
        countJogadas += 1
        return 2,'O'
    else:
        return 1,'X'

def testaSeGanhou():
    # Testa linhas
    for i in range(0, 3):
        if matriz[i] == ['X', 'X', 'X']:
            return 1
        elif matriz[i] == ['O', 'O', 'O']:
            return 2

    # Testa colunas
    for i in range(0, 3):
        if (matriz[0][i] == 'X') and (matriz[1][i] == 'X') and (matriz[2][i] == 'X'):
            return 1
        elif (matriz[0][i] == 'O') and (matriz[1][i] == 'O') and (matriz[2][i] == 'O'):
            return 2

    # Testa diagonais
    if (matriz[0][0] == 'X') and (matriz[1][1] == 'X') and (matriz[2][2] == 'X'):
        return 1
    elif (matriz[0][0] == 'O') and (matriz[1][1] == 'O') and (matriz[2][2] == 'O'):
        return 2
    elif (matriz[0][2] == 'X') and (matriz[1][1] == 'X') and (matriz[2][0] == 'X'):
        return 1
    elif (matriz[0][2] == 'O') and (matriz[1][1] == 'O') and (matriz[2][0] == 'O'):
        return 2
    else:
        return 0

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

def jogando():
    global quemJoga
    global caracter
    global countJogadas
    print("Vez do jogador "+str(quemJoga)+"!")
    linha=input("Linha: ")
    coluna=input("Coluna: ")
    if (int(linha) or int(coluna))<0: msgError()
    else:
        try:
            if matriz[int(linha)][int(coluna)] != " ": msgError2()
            else:
                matriz[int(linha)][int(coluna)]=caracter
                quemJoga,caracter=passaJogador(quemJoga)
        except:
            msgError()
    if countJogadas >= 3:
        vencedor=testaSeGanhou()
    else:
        vencedor=0
    return vencedor

#Inicia com o jogador 1
quemJoga=1
caracter='X'
countJogadas=1
jogarNovamente='s'
matriz=geraMatriz()
while jogarNovamente=='s':
    vencedor=0
    desenhaMatriz()
    vencedor=jogando()
    if (vencedor>0 or countJogadas==5):
        desenhaMatriz()
        print("Jogador",vencedor,"venceu!") if (vencedor>0) else print("It's a draw!")
        jogarNovamente=input("Jogar novamente? (s/n): ")
        if jogarNovamente=='s':
            quemJoga=1
            caracter='X'
            countJogadas=1
            matriz=geraMatriz()
