# *************************************************
# Author:   Tien Li Shen & Daniel Obichie
# date:     2/5/2020
# class:    COMPSCI 383 Artificial Intelligence
# *************************************************
import puzz
import queue
import copy
from time import time

class EightPuzzleBoard_Solver(puzz.EightPuzzleBoard):

    def breadth_search(self, solution):
        if solution is None: #initial condition
            return "invalid goal state"
        # declare variables/objects/lists
        to = time
        frontier = queue.Queue()
        self.add_path(self, "start")
        frontier.put(self)
        explored = []
        frontCount = 1
        # start looping through the breadth
        while not frontier.empty():
            node = frontier.get()       # pop from the frontier
            explored.append(node)       # add the board to the explored list
            for m, n in node.successors().items():      # obtain all possible moves, m = "left", "right", etc. n = puuzzle board
                if n and (n not in explored) and (not self.in_queue(frontier, n)) :
                    n._path = copy.deepcopy(node._path) #deep copy the traveled course
                    n.add_path(n, m)
                    if str(n) == str(solution):         # check if destination reached
                        for k, v in n._path.items():    # loop to print the route
                            print("{}\t{}".format(v,k))
                        return "success:\npath cost: {}\nfrontier: {}\nexplored: {}".format(len(n._path)-1, frontCount, len(explored))
                    else:
                        frontCount += 1
                        frontier.put(n)
        return "fail:\npath cost: {}\nfrontier: {}\nexplored: {}".format(len(n._path)-1, frontCount, len(explored))



    def uniform_cost_search(self, solution, i = 0):
        if solution is None:  # initial condition
            return "invalid goal state"
            # declare variables/objects/lists
        frontier = queue.PriorityQueue()
        self.add_path(self, "start")
        frontier.put((0,self))
        explored = set()
        frontCount = 1
        # start looping through the breadth
        while not frontier.empty():
            pnum, node = frontier.get()     # pop from the frontier
            explored.add(node)           # add the board to the explored list
            if str(node) == str(solution):          # check if destination reached
                for k, v in node._path.items():     # loop to print the route
                    print("{}\t{}".format(v, k))
                return "success:\npath cost: {}\nfrontier: {}\nexplored: {}".format(len(node._path)-1, frontCount, len(explored))
            for m, n in node.successors().items():          # obtain all possible moves, m = "left", "right", etc. n = puuzzle board
                if n and (n not in explored):               # and (not self.in_priority_queue(frontier, n)):
                    n._path = copy.deepcopy(node._path)     # deep copy the traveled course
                    n.add_path(n, m)                        # add new node to the route
                    frontCount += 1
                    frontier.put((len(node._path)-1, n))
                else:
                    self.update_priority_queue(frontier, (len(node._path)-1,n))     # this command checks that if n is in frontier, if frontier(n).cost>n.cost, and updates it
        return "fail:\npath cost: {}\nfrontier: {}\nexplored: {}".format(len(node._path)-1, frontCount, len(explored))


    def greedy_best_first_search(self, solution, i = 0):

        return 0

    def a_star_search(self, solution, i = 0):

        return 0

    def in_queue(self, frontier, n):
        # ******** this section of code checks "n in frontier" ********
        boo = False
        temp = queue.Queue()
        while not frontier.empty():
            node = frontier.get()
            if node is n:
                boo = True
            temp.put(node)
        while not temp.empty():
            frontier.put(temp.get())
        # ********************
        return boo

    def in_priority_queue(self, frontier, n):
        # ******** this section of code checks "n in frontier" ********
        boo = False
        temp = queue.Queue()
        while not frontier.empty():
            node = frontier.get()
            if node[1] is n:
                boo = True
            temp.put(node)
        while not temp.empty():
            frontier.put(temp.get())
        # ********************
        return boo

    def update_priority_queue(self, frontier, n):
        # ******** this section of code checks "n in frontier" ********
        boo = False
        temp = queue.Queue()
        while not frontier.empty():
            node = frontier.get()
            if node[1] is n[1] and node[0] > n[0]:
                temp.put(n)
            else:
                temp.put(node)
        while not temp.empty():
            frontier.put(temp.get())
        # ********************
        return


if __name__ == '__main__':
    board = EightPuzzleBoard_Solver('034615278')
    solution = puzz.EightPuzzleBoard('046315278')
    solution = board.success_up()
    solution = solution.success_left()
    solution = solution.success_left()
    #solution = solution.success_down()



    print(board.uniform_cost_search(solution))
    print("this is solution:{}".format(solution))

