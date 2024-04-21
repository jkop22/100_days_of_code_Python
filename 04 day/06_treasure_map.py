row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\nChoose column and row number (e.g. 33)\n")

col = int(position[0])
row = int(position[1])

map[col-1][row-1] = "X"
print(f"{row1}\n{row2}\n{row3}")