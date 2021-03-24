import numpy as np


count = 0


def solver(bo, type_of_search):
    global count
    if type_of_search == 0:
        find = find_empty_simple_backtrack(bo)
    elif type_of_search == 1:
        find = find_empty_heuristics(bo)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        count = count + 1
        if valid(bo, i, (row, col)):
            bo[row, col] = i
            if solver(bo, type_of_search):
                return True

            bo[row][col] = 0

    return False


def find_empty_heuristics(bo):
    heuristics_matrix = [0 for i in range(81)]
    heuristics_matrix = np.reshape(heuristics_matrix, (9, 9))
    queue = []

    for i in range(9):
        for j in range(9):
            if bo[i, j] != 0:
                queue.append(str(heuristics_matrix[i, j]) + str(i) + str(j))
                continue
            else:
                for y in range(1, 10):
                    if valid(bo, y, (i, j)):
                        heuristics_matrix[i, j] += 1
            queue.append(str(heuristics_matrix[i, j]) + str(i) + str(j))

    queue.sort()

    for i in range(len(queue)):
        if bo[int(queue[i][1]), int(queue[i][2])] == 0:
            return int(queue[i][1]), int(queue[i][2])

    return None


def find_empty_simple_backtrack(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i, j] == 0:
                return i, j  # sor, oszlop

    return None


def valid(bo, num, pos):
    # Sor ellenőrzés
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Oszlop ellenőrzés
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True
