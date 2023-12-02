import sys

total = 0

for line in sys.stdin:
    a = line.split(" ")
    gameID = int(a[1].replace(":", ""))
    b = True

    for i in range(2, len(a), 2):
        num = int(a[i])
        color = a[i + 1].strip(",").strip(";").strip()

        if color == "blue":
            if num > 14:
                b = False
                break
        elif color == "green":
            if num > 13:
                b = False
                break
        else:
            if num > 12:
                b = False
                break

    if b: total += gameID

print(total)