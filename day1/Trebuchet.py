import sys

total = 0
for line in sys.stdin:
    d = ''.join([i for i in line if i.isnumeric()])
    s = d[0] + d[len(d)-1]
    total += int(s)
print(total)