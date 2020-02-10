# *************************************************
# Author:   Tien Li Shen & Daniel Obichie
# date:     2/5/2020
# class:    COMPSCI 383 Artificial Intelligence
# *************************************************
import puzz
import queue

class EightPuzzleBoard_Solver(puzz.EightPuzzleBoard):

    def breadth_search(self, solution):
        #
        frontier = queue.Queue()
        frontier.put(self)
        explored = []
        count = 0
        while not frontier.empty():
            node = frontier.get()
            explored.append(node)
            for m, n in node.successors().items():
                # ******** this section of code checks "n not in frontier" ********
                boo = False
                temp = frontier
                while not temp.empty():
                    node = temp.get()
                    if node is n:
                        boo = True
                # ********************
                if n and (n not in explored) and (not boo) :
                    count += 1
                    if n == solution:
                        return count
                    else:
                        frontier.put(n)
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
    board = EightPuzzleBoard_Solver('346105278')
    solution = puzz.EightPuzzleBoard('046315278')
    solution = board.success_down()
    solution = board.success_left()
    print(board.breadth_search(solution))

   # solution = EightPuzzleBoard('12345678')
   # board.breadth_search(solution)
   # board.uniform_cost_search(solution)

