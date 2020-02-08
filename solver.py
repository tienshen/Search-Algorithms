# *************************************************
# Author:   Tien Li Shen & Daniel Obichie
# date:     2/5/2020
# class:    COMPSCI 383 Artificial Intelligence
# *************************************************
import puzz
import queue

class search(puzz.EightPuzzleBoard):

    def breadth_search(self, solution, i = 0):
        #
        frontier = queue.Queue()
        frontier.put(self)
        explored = []

        while not frontier.empty():
            node = frontier.get()
            explored.append(node)
            for n in node.successors():
                if (n not in frontier) and (n not in explored):
                    if n == solution:
                        return n
                    else:
                        frontier.put(n)
        # if board = goal state:
        # return number of steps
        # x = success up()
        # y = successs down()
        # breadth_search(x)
        # breadth_search(y)
        # ..................
        #
        return "fail"

    def uniform_cost_search(self, solution, i = 0):
        return 0

    def greedy_best_first_search(self, solution, i = 0):
        return 0

    def a_star_search(self, solution, i = 0):
        return 0



if __name__ == '__main__':

    #board = EightPuzzleBoard('12345678')
    board = puzz.EightPuzzleBoard('123450678')
    solution = puzz.EightPuzzleBoard('123450678')
    problm = search('123450678')
    problm.breadth_search(solution)

   # solution = EightPuzzleBoard('12345678')
   # board.breadth_search(solution)
   # board.uniform_cost_search(solution)

