# coding: utf-8

import random
from datas.jsonDatas import JsonDatas

influence = 1
states = (0, 1)
steps = (30, 30)
grid = {}
shema = [(0, 1),
        (1, 2),
        (2, 0), (2, 1), (2, 2),
        (8, 21),
        (9, 20),
        (10, 20), (10, 21), (10, 22),
        (14, 14),
        (15, 15),
        (16, 13), (16, 14), (16, 15)
    ]

for l in range(steps[0]):
    for c in range(steps[1]):
        grid[(l, c)] = 1 if (l, c) in shema else 0
        # grid[(l, c)] = random.choice(states)

"""
Évaluation d'une cellule
"""
# item = (9, 9)
# evalGrid = []

# lItem = item[0] - influence
# cItem = item[1] - influence

# while lItem <= item[0] + influence:
#     if lItem >= 0 and lItem < steps[0]:
#         if cItem >= 0 and cItem < steps[1]:
#             if (lItem, cItem) != item:
#                 evalGrid.append(grid[(lItem, cItem)])

#     if lItem <= item[0] + influence:
#         cItem += 1
#     else:
#         cItem = item[1] - influence
#     if cItem > item[1] + influence:
#         lItem += 1
#         cItem = item[1] - influence

# print(item, evalGrid, evalGrid.count(1))

"""
convertion pour json
"""
gridBackup = {}
for x in grid:
    gridBackup[str(x[0]) + ":" + str(x[1])] = grid[x]

datas = JsonDatas()
datas.writeJson("clock.json", gridBackup)

"""
convertion depuis json
"""
for x in gridBackup:
    coord = x.split(":")
    grid[(int(coord[0]), int(coord[1]))] = gridBackup[x]

