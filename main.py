import time
import solver
import printboard
import readdb


def main():
    sum_nodes = 0
    sum_time = 0

    for x in range(100):
        board = readdb.reformat_csv(readdb.read_from_db()[x])
        printboard.print_board(board)
        solver.count = 0
        start = time.time()
        solver.solver(board, 1)
        end = time.time()
        print("Nodes explored: ", solver.count, " Finished in :", end - start, " second.")
        print("___________________")
        printboard.print_board(board)
        sum_nodes += solver.count
        sum_time += end - start

    avg_nodes = sum_nodes / 100
    avg_time = sum_time / 100
    print("Átlag bejárt állapotok száma: ", avg_nodes)
    print("Átlag futási idő: ", avg_time)


if __name__ == "__main__":
    main()