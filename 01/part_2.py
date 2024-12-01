from collections import defaultdict

left = []
right = defaultdict(int)
simalarity = 0

with open('./input.txt', 'r') as f:
    for line in f:
        left.append(int(line.split()[0]))
        right[(int(line.split()[1]))] += 1

for i in left:
    simalarity += i * right[i]

print(simalarity)