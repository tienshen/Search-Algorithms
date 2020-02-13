# *************************************************
# Author:   Tien Li Shen & Daniel Obichie
# date:     2/5/2020
# class:    COMPSCI 383 Artificial Intelligence
# *************************************************
import puzz
import sys
import queue
import copy
import random
from time import time

class EightPuzzleBoard_Solver(puzz.EightPuzzleBoard):


    def special_search(self, dest, string = "bfs"):
        if dest is None:  # initial condition
            return "invalid goal state, try again"
        if string not in ["bfs", "uniform", "greedy", "astar"]:
            return "invalid algorithm name, please use (bfs, uniform, greedy, astar)"

        frontier = queue.PriorityQueue()
        self.add_path(self, "start")
        frontier.put((0,self))
        explored = set()
        frontCount = 1

        while not frontier.empty():
            pnum, node = frontier.get()     # pop from the frontier
            explored.add(node)           # add the board to the explored list

            if str(node) == str(dest):          # check if destination reached
                for k, v in node._path.items():     # loop to print the route
                    print("{}\t{}".format(v, k))
                return "\nsuccess!\npath cost: {}\nfrontier: {}\nexplored: {}".format(node.get_path_cost(), frontCount, len(explored))

            for m, n in node.successors().items():          # obtain all possible moves, m = "left", "right", etc. n = puuzzle board
                if n and (n not in explored):               # and (not self.in_priority_queue(frontier, n)):
                    n._path = copy.deepcopy(node._path)     # deep copy the traveled course
                    n.add_path(n, m)                        # add new node to the route
                    frontCount += 1
                    frontier.put((node.get_priority_number(dest, string), n))
                # elif string != "bfs":
                #     self.update_priority_queue(frontier, (node.get_path_cost(),n))     # this command checks that if n is in frontier, if frontier(n).cost>n.cost, and updates it

        return "failure"


    def random_dest_generator(self, max):
        n = 0
        current_board = self
        next_board = None
        while n < max:
            successors = current_board.successors()
            while next_board is None:
                rand = random.randint(0,3)
                if rand is 0:
                    next_board = successors["up"]
                elif rand is 1:
                    next_board = successors["down"]
                elif rand is 2:
                    next_board = successors["left"]
                elif rand is 3:
                    next_board = successors["right"]
            n += 1
            current_board = next_board
            next_board = None
        return current_board

if __name__ == '__main__':
    board = EightPuzzleBoard_Solver('034615278')
    dest = board.random_dest_generator(50)
    #sys.argv = [None, 'greedy', '034615278', '345701862'] # try ' python solver.py greedy 034615278 345701862 '
    print(sys.argv)
    if sys.argv[1] and sys.argv[2] and sys.argv[3]:
        string = sys.argv[1]
        board = EightPuzzleBoard_Solver(sys.argv[2])
        dest = EightPuzzleBoard_Solver(sys.argv[3])

    # print("\ngenerated destination: {}\n".format(dest))

    print(board.special_search(dest, string))
