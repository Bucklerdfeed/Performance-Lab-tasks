import sys
with open(sys.argv[1], 'r') as f:
    circ = []
    for line in f:
        line = line.rstrip('\n')
        circ.append(list(map(float,line.split())))

with open(sys.argv[2], 'r') as f:
    dots = []
    for line in f:
        line = line.rstrip('\n')
        dots.append(list(map(float,line.split())))
for i in range(0, len(dots)):
    if (dots[i][0] - circ[0][1]) ** 2 + (dots[i][1] - circ[0][1]) ** 2 > circ[1][0] ** 2:
        print(2)
    elif (dots[i][0] - circ[0][1]) ** 2 + (dots[i][1] - circ[0][1]) ** 2 >= circ[1][0] ** 2:
        print (0)
    else:
        print(1)