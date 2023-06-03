import random
import os
import msvcrt

def random_block():
    a=random.randint(0,len(blocchi)-1)
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
        blocco=[[0,-1],[0,-1],[-1,-1],[0,0]]
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
            #for i in range(len(line)):
            cdx=round(len(line)/2)
            csx=cdx-1
            if griglia_di_gioco[j][csx]!=0 or griglia_di_gioco[j][cdx]!=0:
                return False
            griglia_di_gioco[j][csx]=blocco[j][0]
            griglia_di_gioco[j][cdx]=blocco[j][1]
    return griglia_di_gioco


#def game_over(griglia_di_gioco):
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
    copia_griglia=[]
    rigatmp=[]
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella!=-1:
                rigatmp.append(griglia_di_gioco[r][c])
            else:
                rigatmp.append(0)
        copia_griglia.append(rigatmp)
        rigatmp=[]
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella==-1:
                copia_griglia[r+1][c] = -1
    return copia_griglia

def move_left(griglia_di_gioco):
    copia_griglia=[]
    rigatmp=[]
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella!=-1:
                rigatmp.append(griglia_di_gioco[r][c])
            else:
                rigatmp.append(0)
        copia_griglia.append(rigatmp)
        rigatmp=[]
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella==-1:
                copia_griglia[r][c-1] = -1
    return copia_griglia

def move_right(griglia_di_gioco):
    copia_griglia=[]
    rigatmp=[]
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella!=-1:
                rigatmp.append(griglia_di_gioco[r][c])
            else:
                rigatmp.append(0)
        copia_griglia.append(rigatmp)
        rigatmp=[]
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella==-1:
                copia_griglia[r][c+1] = -1
    return copia_griglia

# funzione che ritorna true se il blocco si puo spostare lungo la direzione, false altrimenti.
def there_is_nothing(griglia_di_gioco, direzione):
    if direzione == 'W':
        shift = 0
    elif direzione == 'D':
        shift = 1
    elif direzione == 'S':
        shift = 1
    elif direzione == 'A':
        shift = -1
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella == -1:
                if direzione == 'D' or direzione=='A' :
                    if griglia_di_gioco[r][c+shift] != 0 and griglia_di_gioco[r][c+shift] != -1:
                        return False
                else :
                    if griglia_di_gioco[r+shift][c] != 0 and griglia_di_gioco[r+shift][c] != -1:
                        return False
    return True

def freeze_block(griglia_di_gioco):
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella==-1:
                griglia_di_gioco[r][c]=1
    return griglia_di_gioco

def check_line(griglia_di_gioco):
    i=linea_piena(griglia_di_gioco)
    while i!=0:
        for c,cella in enumerate(griglia_di_gioco[i]):
            if cella==1:
                griglia_di_gioco[i][c]=0
        griglia_di_gioco[:i]=shift_array(griglia_di_gioco[:i]) 
        i=linea_piena(griglia_di_gioco)
    return griglia_di_gioco

def linea_piena(griglia_di_gioco):
    cont=0
    for r,riga in enumerate(griglia_di_gioco):
        for c,cella in enumerate(riga):
            if cella==1:
                cont=cont+1
        if cont>=(len(riga)-2):
            return r
        cont=0
    return 0

def shift_array(arr): 
    shifted_arr = arr[:1] + [arr[0]] 
    return shifted_arr
#main()
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
griglia_di_gioco=insert_block(next_block(),griglia_di_gioco)
while griglia_di_gioco:
    os.system("cls")
    stampa_griglia(griglia_di_gioco)
    azione=msvcrt.getwch().upper()
    #azione=input("Scegli direzione o rotazione (W,S,D,A): ").upper()
    if azione=="W":
        print()
    elif azione=='S':
        if there_is_nothing(griglia_di_gioco,azione):
            griglia_di_gioco=move_down(griglia_di_gioco)
        else:
            griglia_di_gioco=freeze_block(griglia_di_gioco)
            griglia_di_gioco=check_line(griglia_di_gioco)
            griglia_di_gioco=insert_block(next_block(),griglia_di_gioco)
    elif azione=="D":
        if there_is_nothing(griglia_di_gioco,azione):
            griglia_di_gioco=move_right(griglia_di_gioco)
    elif azione=="A":
        if there_is_nothing(griglia_di_gioco,azione):
            griglia_di_gioco=move_left(griglia_di_gioco)
print("HAI PERSO! :)")