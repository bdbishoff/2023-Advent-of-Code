import sys
import re

total = 0

pattern = r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine|zero))'
d = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}


for line in sys.stdin:
    print(line.strip())
    matches = re.findall(pattern, line)
    print(matches)
    a : str = matches[0]
    b : str = matches[len(matches)-1]

    if not a.isnumeric(): a = d[a]
    if not b.isnumeric(): b = d[b]

    print(a,b, "\n")

    s = str(a) + str(b)

    total += int(s)
print(total)