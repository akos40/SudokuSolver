import numpy as np

count = 0


def solver(bo):
    global count
    find = find_empty_heuristics_forward_checking(bo)

    if not find:
        return True
    else:
        row, col, valid_numbers = find

    for i in range(0, len(valid_numbers)):
        count = count + 1

        if valid(bo, int(valid_numbers[i]), (row, col)):
            bo[row, col] = int(valid_numbers[i])
            if solver(bo):
                return True

            bo[row][col] = 0

    return False


def find_empty_heuristics_forward_checking(bo):
    heuristics_matrix = [0 for i in range(81)]
    heuristics_matrix = np.reshape(heuristics_matrix, (9, 9))
    queue = []

    for i in range(9):
        for j in range(9):
            tmp = ""
            if bo[i, j] != 0:
                queue.append(str(heuristics_matrix[i, j]) + str(i) + str(j))
                continue
            else:
                for y in range(1, 10):
                    if valid(bo, y, (i, j)):
                        heuristics_matrix[i, j] += 1
                        tmp += (str(y))
            queue.append(str(heuristics_matrix[i, j]) + str(i) + str(j) + tmp)

    queue.sort()

    for i in range(len(queue)):
        if bo[int(queue[i][1]), int(queue[i][2])] == 0:
            return int(queue[i][1]), int(queue[i][2]), queue[i][3:]

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
