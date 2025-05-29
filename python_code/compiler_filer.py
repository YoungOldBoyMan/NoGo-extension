import generating_boards as gb


def board_p(b):
    out = ""
    for i in range(gb.BOARD_X):
        for j in range(gb.BOARD_Y):
            if (b[i, j] == 0):
                out += ("open("+str(i)+","+str(j)+") ")
            if (b[i, j] == 1):
                out += ("black("+str(i)+","+str(j)+") ")
            if (b[i, j] == 2):
                out += ("white("+str(i)+","+str(j)+") ")
    return out


# for i in range(3):
#    print("not(" + (board_p(gb.final_boards[i])) + ")")


def as_Sets(b):
    out = set()
    for i in range(gb.BOARD_X):
        for j in range(gb.BOARD_Y):
            if (b[i, j] == 0):
                continue
            if (b[i, j] == 1):
                s = "1"+str(i)+str(j)
                out.add(s)
            if (b[i, j] == 2):
                s = "2"+str(i)+str(j)
                out.add(s)
    return out


list1 = []
for i in range(len(gb.final_boards)):
    list1.append(as_Sets(gb.final_boards[i]))


forbidden_patterns = list1.copy()
for i in range(len(list1)):
    d = list1[i]
    print("Iteration: " + str(i))
    for j in range(len(list1)-1-i):
        sec = list1[j+1+i]
        if (d.issubset(sec)):
            if (list1[j+1+i] in forbidden_patterns):
                forbidden_patterns.remove(list1[j+1+i])


print()
print(len(forbidden_patterns))


def as_string(b):
    out = ""
    for i in b:
        if (i[0] == "0"):
            out += "open("
        if (i[0] == "1"):
            out += "black("
        if (i[0] == "2"):
            out += "white("
        out += str(int(i[1])+1)+","+str(int(i[2])+1)+") "
    return out


endelig = []
for i in range(len(forbidden_patterns)):
    j = as_string(forbidden_patterns[i])
    endelig.append(j)
    # print(j)

with open("1x12_patterns_black.txt", "w") as f:
    for i in endelig:
        f.write(i + "\n")