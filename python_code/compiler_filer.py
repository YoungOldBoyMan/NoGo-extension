import generating_boards as gb




def board_p(b):
    for i in range(2):
        for j in range(3):
            if(b[i,j]==0):
                print("open("+str(i)+","+str(j)+") ")
            if(b[i,j]==1):
                print("black("+str(i)+","+str(j)+") ")
            if(b[i,j]==2):
                print("white("+str(i)+","+str(j)+") ")


for i in range(len(gb.final_boards)):
    print("not(")
    board_p(gb.final_boards[i])
    print(") ")