from itertools import count
fhand = open('Message.txt')
count = 0
inp = fhand.read()
for line in fhand:
    count = count+1
print('Line count', count)
print(inp)
print(inp[:5])
# Reading required lines
