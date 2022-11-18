import sys
with open(sys.argv[1], 'r') as f:
    a = []
    for line in f:
        line = line.rstrip('\n')
        a.append(int(line))
Mi = []
for i in range(len(a)):
    s = 0
    for j in range(len(a)):
        s += abs(a[i] - a[j])
    Mi.append(s)
print(min(Mi))