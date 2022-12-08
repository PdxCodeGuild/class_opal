"""
Note: Assisted by https://github.com/djm4/advent-of-code-2022/blob/main/2022/day/08/solution_a.py
Used that solution to find the right answer and then modified my solution to produce the right answer.
"""

import pandas as pd
import numpy as np

with open(r'C:\Users\jbrennan\Google Drive\Architecture\Tests\pdx_code_guild\fullstack_bootcamp\class_opal\advent-of-code\jim\tree_data.txt') as f:
    tree_data: str = f.read()

tree_data = tree_data.split('\n')

df = pd.DataFrame(tree_data)

df[0] = df[0].str.split("")

for i in range(0, 99):
    df.loc[i, 0] = df.loc[i, 0][1:]

df = pd.DataFrame(df[0].tolist())
df = df.iloc[:, :-1]

down_scores = {}
up_scores = {}
right_scores = {}
left_scores = {}

for i in range(len(df)):
    for j in range(len(df.columns)):
        counter = 1
        for k in range(j + 1, len(df.columns)):
            if int(df[i][j]) > int(df[i][k]):
                counter += 1
            elif int(df[i][j]) == int(df[i][k]):
                counter += 1
                break
            else:
                break
        down_scores[(i, j)] = counter

for i in range(len(df)):
    for j in range(len(df.columns)):
        counter = 0
        for k in reversed(range(0, j)):
            if int(df[i][j]) > int(df[i][k]):
                counter += 1
            elif int(df[i][j]) == int(df[i][k]):
                counter += 1
                break
            else:
                break
        up_scores[(i, j)] = counter


for j in range(len(df.columns)):
    for i in range(len(df)):
        counter = 0
        for k in range(i + 1, len(df.columns)):
            if int(df[i][j]) > int(df[k][j]):
                counter += 1
            elif int(df[i][j]) == int(df[k][j]):
                counter += 1
                break
            else:
                break
        right_scores[(i, j)] = counter

for j in range(len(df.columns)):
    for i in range(len(df)):
        counter = 0
        for k in reversed(range(0, i)):
            if int(df[i][j]) > int(df[k][j]):
                counter += 1
            elif int(df[i][j]) == int(df[k][j]):
                counter += 1
                break
            else:
                break
        left_scores[(i, j)] = counter

scores = {}

for i in range(len(df)):
    for j in range(len(df.columns)):
        scores[(i, j)] = up_scores[(i, j)]*down_scores[(i, j)] * \
            left_scores[(i, j)]*right_scores[(i, j)]

# print(up_scores[(1, 1)])
# print(down_scores[(1, 1)])
# print(left_scores[(1, 1)])
# print(right_scores[(1, 1)])

# print(up_scores[(48, 7)])
# print(down_scores[(48, 7)])
# print(left_scores[(48, 7)])
# print(right_scores[(48, 7)])

# print(scores[(48, 7)])

# value = {i for i in scores if scores[i] == max(list(scores.values()))}
# print("key by value:", value)
# print(scores[value])


print(max(list(scores.values())))
