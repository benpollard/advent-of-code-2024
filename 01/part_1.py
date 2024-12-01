a = []
b = []

distance = 0

with open('./input.txt', 'r') as f:
    for line in f:
        a.append(int(line.split()[0]))
        b.append(int(line.split()[1]))

a.sort()
b.sort()

for i in range(len(a)):
    distance += abs(a[i] - b[i])

print(distance)