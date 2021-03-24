import sqlite3
import numpy as np


def read_from_db():
    con = sqlite3.connect('puzzles.db')
    cur = con.cursor()
    data = [str(row) for row in cur.execute('SELECT * FROM simple')]
    return data


def reformat_csv(puzzle):
    csv_int = [0] * 81
    for i in range(2, 83):
        if puzzle[i] == '.':
            csv_int[i - 2] = 0
        else:
            csv_int[i - 2] = int(puzzle[i])

    csv_int = np.reshape(csv_int, (9, 9))
    return csv_int