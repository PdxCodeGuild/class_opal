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

columns_not_visibile_down = []
columns_not_visibile_up = []
rows_not_visible_right = []
rows_not_visible_left = []

for i in range(len(df)):
    for j in range(len(df.columns)):
        for k in range(j + 1, len(df.columns)):
            if int(df[i][j]) <= int(df[i][k]):
                if (i, j) not in columns_not_visibile_down:
                    columns_not_visibile_down.append((i, j))
                break

for i in range(len(df)):
    for j in range(len(df.columns)):
        for k in range(0, j):
            if int(df[i][j]) <= int(df[i][k]):
                if (i, j) not in columns_not_visibile_up:
                    columns_not_visibile_up.append((i, j))
                break

for j in range(len(df.columns)):
    for i in range(len(df)):
        for k in range(i + 1, len(df.columns)):
            if int(df[i][j]) <= int(df[k][j]):
                if (i, j) not in rows_not_visible_right:
                    rows_not_visible_right.append((i, j))
                break

for j in range(len(df.columns)):
    for i in range(len(df)):
        for k in range(0, i):
            if int(df[i][j]) <= int(df[k][j]):
                if (i, j) not in rows_not_visible_left:
                    rows_not_visible_left.append((i, j))
                break

# print(columns_not_visibile_down)
# print(columns_not_visibile_up)
# print(rows_not_visible_right)
# print(rows_not_visible_left)

not_visible = []

for i in range(len(df)):
    for j in range(len(df.columns)):
        if (i, j) in columns_not_visibile_down and (i, j) in columns_not_visibile_up and (i, j) in rows_not_visible_right and (i, j) in rows_not_visible_left:
            not_visible.append((i, j))
            # print((i, j), df[i][j])

# print(not_visible)

answer = df.size - len(not_visible)

print(answer)
