cols = input("Enter the width of your rectangle")
rows = input("Enter the height of your rectangle")
cols = int(cols)
rows = int(rows)


def print_rectangle(cols, rows):
    for y in range(rows):
        if y:
            print(end="")
        for x in range(cols):
            if x == 0:
                print("|", end="")
            elif x == cols - 1:
                print("|")
            elif y == 0 or y == rows - 1:
                print("-", end="")
            else:
                print(" ", end="")


print_rectangle(cols, rows)
