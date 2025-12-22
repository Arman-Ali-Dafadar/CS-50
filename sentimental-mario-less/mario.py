from cs50 import get_int

while True:
    h = get_int("Height: ")
    if (h > 0) and (h < 9):
        break
i = 1
while (i <= h):
    print(" " * (h-i), end='')
    print("#" * i)
    i = i + 1
