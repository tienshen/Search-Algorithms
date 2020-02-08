# *************************************************
# Author:   Tien Li Shen & Daniel Obichie
# date:     2/5/2020
# class:    COMPSCI 383 Artificial Intelligence
# *************************************************
import puzz.py

class search(EightPuzzleBoard):

    def breadth_search(self, solution, i = 0):
        #
        # if board = goal state:
        # return number of steps
        # x = success up()
        # y = successs down()
        # breadth_search(x)
        # breadth_search(y)
        # ..................
        #
        return str

    def uniform_cost_search(self, solution, i = 0):
        return 0

    def greedy_best_first_search(self, solution, i = 0):
        return 0

    def a_star_search(self, solution, i = 0):




if __name__ == '__main__':
    board = EightPuzzleBoard('12345678')
    solution = EightPuzzleBoard('12345678')
    board.breadth_search(solution)
    board.uniform_cost_search(solution)
