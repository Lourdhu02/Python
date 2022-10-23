count = 0
sum = 0
print('before ', count, sum)
for i in [12, 4, 46, 3, 212, 32]:
    count = count+1
    sum = sum+i
    print(count, sum, i)
print('after ', count, sum, sum/count)
