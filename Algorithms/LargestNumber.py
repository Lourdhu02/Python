largest = -1
print('before ', largest)
for num in [2, 45, 32, 5, 45, 565, 43]:
    if num > largest:
        largest = num
    print(largest, num)
print('after ', largest)
