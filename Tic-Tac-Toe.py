def grid():
    print(f"""
    ---------
    | {tic[0][0]} {tic[0][1]} {tic[0][2]} |
    | {tic[1][0]} {tic[1][1]} {tic[1][2]} |
    | {tic[2][0]} {tic[2][1]} {tic[2][2]} |
    ---------""")


tic = [[" "]*3 for i in range(3)]
con = 2
while True:
    boom = input("Enter the coordinates: ")
    n = [x for x in boom.split() if x.isalpha()]
    h_line_1 = "".join(tic[0][0:])
    h_line_2 = "".join(tic[1][0:])
    h_line_3 = "".join(tic[2][0:])
    g_line_1 = "".join(tic[0:][0])
    g_line_2 = "".join(tic[0:][1])
    g_line_3 = "".join(tic[0:][2])
    hl_line_1 = tic[0][0] + tic[1][1] + tic[2][2]
    ls = h_line_1, h_line_2, h_line_3, g_line_1, g_line_2, g_line_3, tic[0][0] + tic[1][1] + tic[2][2], tic[0][2] + tic[1][1] + tic[2][0]
    if "XXX" in ls:
        print("X wins")
        break
    if "OOO" in ls:
        print("O wins")
        break
    if con >= 11:
        print("Draw")
        break
    if len(n) > 0:
        print("You should enter numbers!")
    else:
        x, y = boom.split()
        x, y = int(x), int(y)
        if x > 3 or y > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if tic[x - 1][y - 1] != " ":
                print("This cell is occupied! Choose another one!")
            elif con % 2 == 0:
                tic[x - 1][y - 1] = "X"
                grid()
                con += 1
            else:
                tic[x - 1][y - 1] = "O"
                grid()
                con += 1
