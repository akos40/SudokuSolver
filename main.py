import time
import solver
import printboard
import readdb
import forwardChecking


def main():
    sum_nodes = 0
    sum_time = 0

    for x in range(100):
        board = readdb.reformat_csv(readdb.read_from_db()[x])
        printboard.print_board(board)
        forwardChecking.count = 0
        start = time.time()
        forwardChecking.solver(board)
        end = time.time()
        print("Nodes explored: ", forwardChecking.count, " Finished in :", end - start, " second.")
        print("___________________")
        printboard.print_board(board)
        sum_nodes += forwardChecking.count
        sum_time += end - start

    avg_nodes = sum_nodes / 100
    avg_time = sum_time / 100
    print("Átlag bejárt állapotok száma: ", avg_nodes)
    print("Átlag futási idő: ", avg_time)


if __name__ == "__main__":
    main()
