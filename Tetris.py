import random
import os
import copy

def random_block():
    a=random.randint(0,len(blocchi))
    print(a)
    return blocchi[a]

def next_block():
    a=random_block()
    if a==blocchi[0]:
        blocco=[[-1,0],[-1,0],[-1,-1],[0,0]]
        return blocco
    elif a==blocchi[1]:
        blocco=[[0,-1],[-1,-1],[0,-1],[0,0]]
        return blocco
    elif a==blocchi[2]:
        blocco=[[-1,0],[-1,-1],[0,-1],[0,0]]
        return blocco
    elif a==blocchi[3]:
        blocco=[[-1,0],[-1,0],[-1,0],[-1,0]]
        return blocco
    elif a==blocchi[4]:
        blocco=[[0,-1],[-1,-1],[-1,0],[0,0]]
        return blocco
    elif a==blocchi[5]:
        blocco=[[0,-1],[0,-1],[-1,-1][0,0]]
        return blocco
    elif a==blocchi[6]:
        blocco=[[-1,-1],[-1,-1],[0,0],[0,0]]
        return blocco
    
def stampa_griglia(griglia):
    for linea in griglia:
        for casella in linea:
            if casella==0:
                print(" ",end="")
            elif casella==2:
                print("o",end="")
            else:
                print("X",end="")
        print()

def insert_block(blocco,griglia_di_gioco):
    for j,line in enumerate(griglia_di_gioco):
        if j<len(blocco):  
            for i in range(len(line)):
                cdx=round(len(line)/2)
                csx=cdx-1
                griglia_di_gioco[j][csx]=blocco[j][0]
                griglia_di_gioco[j][cdx]=blocco[j][1]
    return griglia_di_gioco


def game_over(griglia_di_gioco):
    count=[]
    nrighe=0
    ncolonne=0
    for j,line in enumerate(griglia_di_gioco):
        ncolonne=len(line)-2
        nrighe=j
    for t in range(ncolonne+2):
        count.append(0)
    for j in range(1,ncolonne):
        for i in range(nrighe):
            if griglia_di_gioco[i][j]==1:
                count[j]=count[j]+1
    print(count)
    for c in count:
        if c>=nrighe:
            return True
    return False

def move_down(griglia_di_gioco):
    copia_griglia=copy.copy(griglia_di_gioco)
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella==-1:
                copia_griglia[r+1][c] = -1
    return copia_griglia

#main()
print("Ciao")
print("Come va?")
griglia_di_gioco=[[2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,0,0,0,0,0,0,0,0,2],
                  [2,2,2,2,2,2,2,2,2,2]]
blocchi=["L","T","S","I","Z","J","Q"]
while not game_over(griglia_di_gioco):
    griglia_di_gioco=insert_block(next_block(),griglia_di_gioco)
    os.system("cls")
    stampa_griglia(griglia_di_gioco)
    azione=input("Scegli direzione o rotazione (W,S,D,A): ").upper()
    if azione=="W":
        print()
    elif azione=="S":
        griglia_di_gioco=move_down(griglia_di_gioco)
    elif azione=="D":
        print()
    elif azione=="A":
        print()