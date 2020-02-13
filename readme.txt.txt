Name: Tien Li Shen & Daniel Obichie

Date: 2/13/2020

What is the best meal you have ever eaten?

Tien: 小籠包(xia long boa) and 牛肉麵(beef noodle soup) from 鼎泰豐 (ding tai fung)

Daniel: Nigerian cassava and soup cuisine

A short (3-4 sentence) summary of findings from examining the performance metrics on
different test cases. Which methods are most efficient? How does the choice of
heuristic affect results?

From testing each methods, I think that A* is the most efficient, with greedy, uniform, and BFS in descending efficiency order. 
I think heuristic predicts the best next move very well, which contribute to better overall performance. A* is better than greedy in the way that it also tracks current cost and better performance really shows in my test. Uniform is slightly better than BFS in that it uses current cost to prioritize.

In our code, all 4 search algorithms are working. please use 'python solver.py bfs 123456780 087654321 ' format to run the code.

'bfs' can be replaced with 'uniform' 'greedy' or 'astar'