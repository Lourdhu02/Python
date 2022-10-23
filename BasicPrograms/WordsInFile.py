from itertools import count


fname = 'Message.txt'
fhand = open(fname)
di = dict()
for line in fhand:
    wds = line.split()
    line = line.rstrip('\n')
    for w in wds:
        di[w] = di.get(w, 0)+1

print(di)
x = sorted(di.items())
print(x)
