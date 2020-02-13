# *************************************************
# Author:   Tien Li Shen & Daniel Obichie
# date:     2/5/2020
# class:    COMPSCI 383 Artificial Intelligence
# *************************************************
import puzz
import queue
import copy
import random
from time import time

class EightPuzzleBoard_Solver(puzz.EightPuzzleBoard):

    # def breadth_search(self, solution):
    #     if solution is None: #initial condition
    #         return "invalid goal state"
    #     # declare variables/objects/lists
    #     to = time
    #     frontier = queue.Queue()
    #     self.add_path(self, "start")
    #     frontier.put(self)
    #     explored = []
    #     frontCount = 1
    #     # start looping through the breadth
    #     while not frontier.empty():
    #         node = frontier.get()       # pop from the frontier
    #         explored.append(node)       # add the board to the explored list
    #         for m, n in node.successors().items():      # obtain all possible moves, m = "left", "right", etc. n = puuzzle board
    #             if n and (n not in explored) and (not self.in_queue(frontier, n)) :
    #                 n._path = copy.deepcopy(node._path) #deep copy the traveled course
    #                 n.add_path(n, m)
    #                 if str(n) == str(solution):         # check if destination reached
    #                     for k, v in n._path.items():    # loop to print the route
    #                         print("{}\t{}".format(v,k))
    #                     return "success:\npath cost: {}\nfrontier: {}\nexplored: {}".format(len(n._path)-1, frontCount, len(explored))
    #                 else:
    #                     frontCount += 1
    #                     frontier.put(n)
    #     return "fail:\npath cost: {}\nfrontier: {}\nexplored: {}".format(len(n._path)-1, frontCount, len(explored))



    def special_search(self, dest, string = "bfs"):
        if dest is None:  # initial condition
            return "invalid goal state"
            # declare variables/objects/lists
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


    # def in_queue(self, frontier, n):
    #     # ******** this section of code checks "n in frontier" ********
    #     boo = False
    #     temp = queue.Queue()
    #     while not frontier.empty():
    #         node = frontier.get()
    #         if node is n:
    #             boo = True
    #         temp.put(node)
    #     while not temp.empty():
    #         frontier.put(temp.get())
    #     # ********************
    #     return boo
    #
    # def in_priority_queue(self, frontier, n):
    #     # ******** this section of code checks "n in frontier" ********
    #     boo = False
    #     temp = queue.Queue()
    #     while not frontier.empty():
    #         node = frontier.get()
    #         if node[1] is n:
    #             boo = True
    #         temp.put(node)
    #     while not temp.empty():
    #         frontier.put(temp.get())
    #     # ********************
    #     return boo
    #
    # def update_priority_queue(self, frontier, n):
    #     # ******** this section of code checks "n in frontier" ********
    #     boo = False
    #     temp = queue.Queue()
    #     while not frontier.empty():
    #         node = frontier.get()
    #         if node[1] is n[1] and node[0] > n[0]:
    #             temp.put(n)
    #         else:
    #             temp.put(node)
    #     while not temp.empty():
    #         frontier.put(temp.get())
    #     # ********************
    #     return


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

    # solution = board.success_up()
    # solution = solution.success_left()
    # solution = solution.success_left()
    # string = sys.argv[1]
    # board = EightPuzzleBoard_Solver(sys.argv[2])
    # dest = sys.argv[3]
    print("\ngenerated destination: {}\n".format(dest))


    print(board.special_search(dest, "greedy"))
