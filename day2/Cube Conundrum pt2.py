import sys

total = 0
ptotal = 0

for line in sys.stdin:
    d = {"red": 0, "green": 0, "blue": 0}
    a = line.split(" ")
    gameID = int(a[1].replace(":", ""))

    for i in range(2, len(a), 2):
        num = int(a[i])
        color = a[i + 1].strip(",").strip(";").strip()
        if d[color] < num: d[color] = num

    v = 1
    for k,values in d.items():
        if values == 0:
            continue
        v *= values

    ptotal += v

print(ptotal)
