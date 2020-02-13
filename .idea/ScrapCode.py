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