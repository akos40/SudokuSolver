import numpy as np
import csv
import time


def solve_heuristics(bo):
    global count
    find = find_empty_heuristics(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        count = count + 1
        if valid(bo, i, (row, col)):
            bo[row, col] = i
            if solve_heuristics(bo):
                return True

            bo[row][col] = 0

    return False


def solve_backtrack(bo):
    global count
    find = find_empty_simple_backtrack(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        count = count + 1
        if valid(bo, i, (row, col)):
            bo[row, col] = i
            if solve_backtrack(bo):
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


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end='')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end='')


with open('expert.csv', newline="") as f:
    reader = csv.reader(f)
    data = [str(row) for row in reader]


def reformat_csv(puzzle):
    csv_int = [0] * 81
    for i in range(2, 83):
        if puzzle[i] == '.':
            csv_int[i - 2] = 0
        else:
            csv_int[i - 2] = int(puzzle[i])

    csv_int = np.reshape(csv_int, (9, 9))
    return csv_int


sum_nodes = 0
sum_time = 0

for x in range(1):
    board = reformat_csv(data[x])
    print_board(board)
    count = 0
    start = time.time()
    solve_heuristics(board)
    end = time.time()
    print("Nodes explored: ", count, " Finished in :", end - start, " second.")
    print("___________________")
    print_board(board)
    print("done")
    sum_nodes += count
    sum_time += end - start

avg_nodes = sum_nodes / 20
avg_time = sum_time / 20
print("Átlag bejárt állapotok száma: ", avg_nodes)
print("Átlag futási idő: ", avg_time)
