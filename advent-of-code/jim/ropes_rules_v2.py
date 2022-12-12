with open(r'C:\Users\jbrennan\Google Drive\Architecture\Tests\pdx_code_guild\fullstack_bootcamp\class_opal\advent-of-code\jim\rope_data.txt') as f:
    rope_data: str = f.read()

rope_data = rope_data.split('\n')

new_rope_data = []
for pair in rope_data:
    pair = pair.split(" ")
    pair[1] = int(pair[1])
    new_rope_data.append(pair)

h_pos = (0, 0)
t_pos = (0, 0)

h_cover = [(0, 0)]
t_cover = [(0, 0)]

for step in new_rope_data:
    # calculate h pos
    if step[0] == 'R':
        for i in range(1, step[1] + 1):
            h_cover.append((h_pos[0]+i, h_pos[1]))
        h_pos = (h_pos[0]+step[1], h_pos[1])
    elif step[0] == 'L':
        for i in range(1, step[1] + 1):
            h_cover.append((h_pos[0]-i, h_pos[1]))
        h_pos = (h_pos[0]-step[1], h_pos[1])
    elif step[0] == 'U':
        for i in range(1, step[1] + 1):
            h_cover.append((h_pos[0], h_pos[1]+i))
        h_pos = (h_pos[0], h_pos[1]+step[1])
    elif step[0] == 'D':
        for i in range(1, step[1] + 1):
            h_cover.append((h_pos[0], h_pos[1]-i))
        h_pos = (h_pos[0], h_pos[1]-step[1])

h_pos = (0, 0)


def get_cover(t_pos, h_pos, h_cover, t_cover):

    for t in range(len(h_cover) - 1):
        if h_pos == t_pos:
            pass

        # when h is right of t and h moves up, down, or left, t does not move
        # h_pos right of t_pos, h moves right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]:
            t_pos = (t_pos[0] + 1, t_pos[1])
            t_cover.append(t_pos)
            pass

        # when h is right of t and h moves up-left or down-left, t does not move
        # when h is right of t and h moves up-right, t moves up-right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0] + 1, t_pos[1]+1)
            t_cover.append(t_pos)
            pass

        # when h is right of t and h moves down-right, t moves down-right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] + 1, t_pos[1]-1)
            t_cover.append(t_pos)
            pass

        # when h is left of t and h moves up, down, or right, t does not move
        # when h is left of t and h moves left, t moves left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]:
            t_pos = (t_pos[0] - 1, t_pos[1])
            t_cover.append(t_pos)
            pass

        # when h is left of t and h moves up-right or down-right, t does not move
        # when h is left of t and h moves up-left, t moves up-left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0] - 1, t_pos[1]+1)
            t_cover.append(t_pos)
            pass

        # when h is left of t and h moves down-left, t moves down-left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] - 1, t_pos[1]-1)
            t_cover.append(t_pos)
            pass

        # when h is above t and h moves left, down, or right, t does not move
        # when h is above t and h moves up, t moves up
        elif t_pos[0] == h_pos[0] and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] and h_cover[t+1][1] == h_pos[1] + 1:
            t_pos = (t_pos[0], t_pos[1] + 1)
            t_cover.append(t_pos)
            pass

        # when h is above t and h moves down-right or down-left, t does not move
        # when h is above t and h moves up-left, t moves up-left
        elif t_pos[0] == h_pos[0] and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0] - 1, t_pos[1]+1)
            t_cover.append(t_pos)
            pass

        # when h is above t and h moves up-right, t moves up-right
        elif t_pos[0] == h_pos[0] and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0] + 1, t_pos[1]+1)
            t_cover.append(t_pos)
            pass

        # when h is below t and h moves left, up, or right, t does not move
        # when h is below t and h moves down, t moves down
        elif t_pos[0] == h_pos[0] and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] and h_cover[t+1][1] == h_pos[1] - 1:
            t_pos = (t_pos[0], t_pos[1] - 1)
            t_cover.append(t_pos)
            pass

        # when h is below t and h moves up-right or up-left, t does not move
        # when h is below t and h moves down-left, t moves down-left
        elif t_pos[0] == h_pos[0] and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] - 1, t_pos[1]-1)
            t_cover.append(t_pos)
            pass

        # when h is below t and h moves down-right, t moves down-right
        elif t_pos[0] == h_pos[0] and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] + 1, t_pos[1]-1)
            t_cover.append(t_pos)
            pass

        # when h is up and right of t and h moves left or down, t does not move
        # when h is up and right of t, and h moves up, t moves up and right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] and h_cover[t+1][1] == h_pos[1] + 1:
            t_pos = (t_pos[0] + 1, t_pos[1] + 1)
            t_cover.append(t_pos)
            pass

        # when h is up and right of t, and h moves right, t moves up and right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]:
            t_pos = (t_pos[0] + 1, t_pos[1] + 1)
            t_cover.append(t_pos)
            pass

        # when h is up and right of t and h moves down-left, t does not move
        # when h is up and right of t, and h moves up-right, t moves up and right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0] + 1, t_pos[1] + 1)
            t_cover.append(t_pos)
            pass

        # when h is up and right of t, and h moves down-right, t moves right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] + 1, t_pos[1])
            t_cover.append(t_pos)
            pass

        # when h is up and right of t, and h moves up-left, t moves up
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0], t_pos[1]+1)
            t_cover.append(t_pos)
            pass

        # when h is up and left of t and h moves right or down, t does not move
        # when h is up and left of t, and h moves left, t moves up and left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]:
            t_pos = (t_pos[0] - 1, t_pos[1] + 1)
            t_cover.append(t_pos)
            pass

        # when h is up and left of t, and h moves up, t moves up and left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] and h_cover[t+1][1] == h_pos[1] + 1:
            t_pos = (t_pos[0] - 1, t_pos[1] + 1)
            t_cover.append(t_pos)
            pass

        # when h is up and left of t and h moves down-right, t does not move
        # when h is up and left of t, and h moves up-left, t moves up and left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0] - 1, t_pos[1] + 1)
            t_cover.append(t_pos)
            pass

        # when h is up and left of t, and h moves down-left, t moves left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] - 1, t_pos[1])
            t_cover.append(t_pos)
            pass

        # when h is up and left of t, and h moves up-right, t moves up
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] - 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0], t_pos[1]+1)
            t_cover.append(t_pos)
            pass

        # when h is down and right of t and h moves left or up, t does not move
        # when h is down and right of t, and h moves down, t moves down and right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] and h_cover[t+1][1] == h_pos[1] - 1:
            t_pos = (t_pos[0] + 1, t_pos[1] - 1)
            t_cover.append(t_pos)
            pass

        # when h is down and right of t, and h moves right, t moves down and right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]:
            t_pos = (t_pos[0] + 1, t_pos[1] - 1)
            t_cover.append(t_pos)
            pass

        # when h is down and right of t and h moves up-left, t does not move
        # when h is down and right of t, and h moves down-right, t moves down and right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] + 1, t_pos[1] - 1)
            t_cover.append(t_pos)
            pass

        # when h is down and right of t, and h moves down-left, t moves down
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0], t_pos[1]-1)
            t_cover.append(t_pos)
            pass

        # when h is down and right of t, and h moves up-right, t moves right
        elif t_pos[0] == h_pos[0] - 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0]+1, t_pos[1])
            t_cover.append(t_pos)
            pass

        # when h is down and left of t and h moves right or up, t does not move
        # when h is down and left of t, and h moves down, t moves down and left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] and h_cover[t+1][1] == h_pos[1] - 1:
            t_pos = (t_pos[0] - 1, t_pos[1] - 1)
            t_cover.append(t_pos)
            pass

        # when h is down and left of t, and h moves left, t moves down and left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]:
            t_pos = (t_pos[0] - 1, t_pos[1] - 1)
            t_cover.append(t_pos)
            pass

        # when h is down and left of t and h moves up-right, t does not move
        # when h is down and left of t, and h moves down-left, t moves down and left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0] - 1, t_pos[1] - 1)
            t_cover.append(t_pos)
            pass

        # when h is down and left of t, and h moves down-right, t moves down
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] + 1 and h_cover[t+1][1] == h_pos[1]-1:
            t_pos = (t_pos[0], t_pos[1]-1)
            t_cover.append(t_pos)
            pass

        # when h is down and left of t, and h moves up-left, t moves left
        elif t_pos[0] == h_pos[0] + 1 and t_pos[1] == h_pos[1] + 1 and h_cover[t+1][0] == h_pos[0] - 1 and h_cover[t+1][1] == h_pos[1]+1:
            t_pos = (t_pos[0]-1, t_pos[1])
            t_cover.append(t_pos)
            pass

        h_pos = h_cover[t + 1]

    return t_cover


cover_1 = get_cover(t_pos, h_pos, h_cover, t_cover)
cover_2 = get_cover(t_pos, h_pos, cover_1, [(0, 0)])
cover_3 = get_cover(t_pos, h_pos, cover_2, [(0, 0)])
cover_4 = get_cover(t_pos, h_pos, cover_3, [(0, 0)])
cover_5 = get_cover(t_pos, h_pos, cover_4, [(0, 0)])
cover_6 = get_cover(t_pos, h_pos, cover_5, [(0, 0)])
cover_7 = get_cover(t_pos, h_pos, cover_6, [(0, 0)])
cover_8 = get_cover(t_pos, h_pos, cover_7, [(0, 0)])
cover_9 = get_cover(t_pos, h_pos, cover_8, [(0, 0)])


print(h_cover)
print(cover_1)
print(cover_2)

print(len(set(cover_9)))
