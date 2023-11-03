import sys

input = sys.stdin.readlines()
count = 0
get_division_point = False
DP = [42,42]  #DivisionPoint

for line in input:
    if count == 0:
        count = int(line[0])
        #print("Count: {}".format(count))
        if count == 0:
            break
        get_division_point = True
        #print("getDP: {}".format(get_division_point))
        continue
    temp = line.split()
    a = int(temp[0])
    b = int(temp[1])
    if get_division_point:
        DP[0] = a
        DP[1] = b
        #print("DP: {},{}".format(DP[0], DP[1]))
        get_division_point = False
        continue
    count = count-1
    #print("DP: {},{} and Point {},{} gets to".format(DP[0], DP[1], a, b))
    if a == DP[0] or b == DP[1]:
        print("divisa")
        continue
    if a < DP[0]:
        if b < DP[1]:
            print("SO")
            continue
        print("NO")
        continue
    if b > DP[1]:
        print("NE")
        continue
    print("SE")