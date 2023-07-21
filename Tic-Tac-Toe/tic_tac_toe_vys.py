#displaying the matrix
def disp():
    for i in range(n):
        print("\n")
        for j in range(n):
            print("\t",ini_matr[i][j],end = "\t")

#player input and customization of matrix
def do_player(player):
    if player==1:
        c = True
        while(c):
            a,b = map(int,input("\nPLAYER 1:\n\nENTER THE ROW,COL NUMBER (eg: 1 2 *give space between each): ").split())
            a,b = a-1,b-1
            if a<0 or b<0 or a>2 or b>2:
                c = True
                print("\nINVALID ROW/COL\n")
            else:
                if ini_matr[a][b]=='[]':
                    ini_matr[a][b]='X'
                    c = False
                elif ini_matr[a][b]=='O':
                    print("\nALREADY SELECTED BY PLAYER 2\n")
                    c = True
                else:
                    print("\nSELECTED ALREADY\n")
                    c = True
    else:
        d = True
        while(d):
            a1,b1 = map(int,input("\nPLAYER 2:\n\nENTER THE ROW,COL NUMBER (eg: 1 2 *give space between each): ").split())
            a1 = a1-1
            b1 = b1-1
            if a1<0 or b1<0 or a1>2 or b1>2:
                d = True
                print("\nINVALID ROW/COL\n")
            else:
                if ini_matr[a1][b1]=='[]':
                    ini_matr[a1][b1]='O'
                    d = False
                elif ini_matr[a1][b1]=='X':
                    print("\nALREADY SELECTED BY PLAYER 1\n")
                    d = True
                else:
                    print("\nSELECTED ALREADY\n")
                    d = True
    
#checking the diagonal from left to right
def left_rig_diag(ini_matr):
    pl1 = True
    pl2 = True
    j = 0
    for i in range(n):
        if pl1==True:
            if ini_matr[i][j]!='X':
                pl1 = False
        if pl2==True:
            if ini_matr[i][j]!='O':
                pl2 = False
        j = j + 1
    if pl1:
        return 'X'
    elif pl2:
        return 'O'
    else:
        return '[]'

#checking the diagonal from right to left
def rig_left_diag(ini_matr):
    pl1 = True
    pl2 = True
    j = n-1
    for i in range(n):
        if pl1==True:
            if ini_matr[i][j]!='X':
                pl1 = False
        if pl2==True:
            if ini_matr[i][j]!='O':
                pl2 = False
        j = j - 1
    if pl1:
        return 'X'
    elif pl2:
        return 'O'
    else:
        return '[]'

#checking row wise
def row_wise_check():
    for i in range(n):
        frst = ini_matr[i][0]
        frst_list = ini_matr[i]
        if frst_list.count(frst)==3 and frst!='[]':
            return frst

#checking column wise
def col_wise_check(grid):
    for i in range(n):
        if grid[0][i] == grid[1][i] == grid[2][i] != '[]':
            return grid[0][i]
        
print("\n\n\t\t---------------------------")
print("\t\tWELCOME TO TIC-TAC-TOE GAME\t\tBY : VYSAKH S")
print("\t\t---------------------------\n") 

#creating or initializing the empty/null matrix
n = 3
ini_matr = []
for i in range(n):
    sub_mat = []
    for j in range(n):
        sub_mat.append('[]')
    ini_matr.append(sub_mat)

print("\nINITIAL MATRIX :-\n\t")
disp()
print("\n")

res = '[]'
tot_count = 0
rounds = 0
#continue when the res value []
while(res!='X' or res!='O'):
    rounds += 1
    
    #player1 game play
    do_player(1)
                
    print("\nUPDATED MATRIX :-\n\t")
    disp()
    print("\n")
    
    res = left_rig_diag(ini_matr)
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    res = rig_left_diag(ini_matr)
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    res = row_wise_check()
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    res = col_wise_check(ini_matr)
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    tot_count += 1
    if tot_count == 9:
        print("\n\n\t\tTIE GAME\n\n")
        break

    #player2 game play
    do_player(2)       
    print("\nUPDATED MATRIX :-\n\t")
    disp()
    print("\n")
    
    res = left_rig_diag(ini_matr)
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    res = rig_left_diag(ini_matr)
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    res = row_wise_check()
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    res = col_wise_check(ini_matr)
    if res=='X':
        print("\n\n\t\tPLAYER 1 WON\n\n")
        break
    elif res=='O':
        print("\n\n\t\tPLAYER 2 WON\n\n")
        break
    
    tot_count += 1

if tot_count!=9:
    print("\n\n\t  ATTEMPTS MADE TO WIN : ",rounds,"\n\n")
          
print("\n\n\t\t-----------------------")
print("\t\tEND OF TIC-TAC-TOE GAME")
print("\t\t-----------------------\n")

