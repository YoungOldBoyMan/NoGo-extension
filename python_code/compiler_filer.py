import generating_boards as gb


def board_p(b):
    out = ""
    for i in range(3):
        for j in range(3):
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
    for i in range(3):
        for j in range(3):
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


nyliste = list1.copy()
for i in range(len(list1)):
    d = list1[i]
    for j in range(len(list1)-1-i):
        sec = list1[j+1+i]
        if (d.issubset(sec)):
            if (list1[j+1+i] in nyliste):
                nyliste.remove(list1[j+1+i])


print()
print(nyliste)


def as_string(b):
    out = ""
    for i in b:
        if (i[0] == "0"):
            out += "open("
        if (i[0] == "1"):
            out += "black("
        if (i[0] == "2"):
            out += "white("
        out += i[1]+","+i[2]+") "
    return out


endelig = []
for i in range(len(nyliste)):
    j = as_string(nyliste[i])
    endelig.append(j)
    print(j)

print(len(endelig))
