# coding: utf-8

import random
from datas.jsonDatas import JsonDatas

influence = 1
states = (0, 1)
steps = (10, 10)
grid = {}

for l in range(steps[0]):
    for c in range(steps[1]):
        grid[(l, c)] = random.choice(states)

item = (9, 9)
evalGrid = []

lItem = item[0] - influence
cItem = item[1] - influence

while lItem <= item[0] + influence:
    if lItem >= 0 and lItem < steps[0]:
        if cItem >= 0 and cItem < steps[1]:
            if (lItem, cItem) != item:
                evalGrid.append(grid[(lItem, cItem)])

    if lItem <= item[0] + influence:
        cItem += 1
    else:
        cItem = item[1] - influence
    if cItem > item[1] + influence:
        lItem += 1
        cItem = item[1] - influence

print(item, evalGrid, evalGrid.count(1))

"""
convertion pour json
"""
# gridBackup = {}
# for x in grid:
#     gridBackup[str(x[0]) + ":" + str(x[1])] = grid[x]

"""
convertion depuis json
"""
# for x in gridBackup:
#     coord = x.split(":")
#     grid[(int(coord[0]), int(coord[1]))] = gridBackup[x]