import re
hand = open('Message.txt')  # type: ignore
x = 'Hi miss 79 nice to meet you i think its 98 is your attendance'
for line in hand:
    line = line.rstrip()
    if re.search('Hi', line):
        print("Found")
    else:
        print("Not found")

y = re.findall('[0-9]+', x)
z = re.findall('[aeiou]+', x)
# regression funtion which find the required value in the string
print(y)
print(z)
