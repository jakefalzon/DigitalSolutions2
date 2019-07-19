from random import randint

lot_nums = [[0] * 6]

for i in range(len(lot_nums)):
    for j in range(len(lot_nums[i])):
        lot_nums[i][j] = randint(1, 50)


for x in range(len(lot_nums)):
    print(lot_nums[x])

