def count_trees(data: str):
    visible_trees = []
    lines = data.split('\n')
    trees = [[int(n) for n in line] for line in lines]

    for i in (range(len(trees))):
        # from the left
        current_max = -1
        for j in range(len(trees[i])):
            trees_so_far = trees[i][:j+1]
            if max(trees_so_far) > current_max:
                current_max = max(trees_so_far)
                visible_trees.append((i, j))

        # from the right
        current_max = -1
        for j in range(len(trees[i])):
            trees_so_far = trees[i][:-j-2:-1]
            if max(trees_so_far) > current_max:
                current_max = max(trees_so_far)
                visible_trees.append((i, (len(trees[i])-1)-j))

    for i in range(len(trees[0])):
        column = [row[i] for row in trees]

        # from the top
        current_max = -1
        for j in range(len(column)):
            trees_so_far = column[:j+1]
            # print(trees_so_far)
            if max(trees_so_far) > current_max:
                current_max = max(trees_so_far)
                visible_trees.append((j, i))

        # from the bottom
        current_max = -1
        for j in range(len(column)):
            trees_so_far = column[:-j-2:-1]
            if max(trees_so_far) > current_max:
                current_max = max(trees_so_far)
                visible_trees.append((len(trees[i])-1-j, i))

    return len(set(visible_trees))


def tree_score(data: str):
    lines = data.split('\n')
    trees = [[int(n) for n in line] for line in lines]
    scores = []
    for i in range(len(trees)):
        if i == 0 or i == len(trees)-1:
            pass
        else:
            for j in range(len(trees[1])):
                self_tree = trees[i][j]

                # look up
                distance = 1
                up_trees = 0
                while True:
                    up_trees += 1
                    compare = trees[i-distance][j]
                    if compare >= self_tree or i-distance == 0:
                        break
                    distance += 1

                # look down
                distance = 1
                down_trees = 0
                while True:
                    down_trees += 1
                    compare = trees[i+distance][j]
                    if compare >= self_tree or i+distance == len(trees)-1:
                        break
                    distance += 1

                # look right
                if j+1 == len(trees[i]):
                    break
                distance = 1
                right_trees = 0
                while True:
                    right_trees += 1
                    compare = trees[i][j+distance]
                    if compare >= self_tree or j+distance == len(trees[i])-1:
                        break
                    distance += 1

                # look left
                distance = 1
                left_trees = 0
                while True:
                    if j == 0:
                        break
                    left_trees += 1
                    compare = trees[i][j-distance]
                    if compare >= self_tree or j-distance == 0:
                        break
                    distance += 1

                score = up_trees * down_trees * left_trees * right_trees
                scores.append(score)

    return max(scores)


if __name__ == '__main__':
    with open('advent-of-code/danny/day8/input.txt') as f:
        data: str = f.read()
    print(count_trees(data))
    print(tree_score(data))
