from heap import Heap, HeapData
from maze import Maze
from queue import Queue
from stack import Stack
import numpy as np


class Probe:
    def __init__(self, ptype, maze):
        self.type = ptype  # 1 = BFS and 2 = DFS 3 = Dijkstra
        self.maze = maze

        # array to record which rooms have been visited
        self.visited = [None] * self.maze.size
        for i in range(0, self.maze.size):
            self.visited[i] = [None] * self.maze.size
            for j in range(0, self.maze.size):
                self.visited[i][j] = False
        self.found = False

    def __str__(self):
        if self.type == 1:
            ptype = "breadth-first search"
        elif self.type == 2:
            ptype = "depth-first search"
        else:
            ptype = "dijkstra"

        return "A " + ptype + " probe"

    # performs different search algorithm based on type of probe
    def search(self, x, y, target):
        if self.type == 1:
            self.bfs(x, y)
        elif self.type == 2:
            self.dfs(x, y)
        else:
            # only if Player has map
            self.dijkstra(x, y, target)

    def bfs(self, start_x, start_y):
        queue = Queue()
        last = None
        path_dict = {last: None}

        # adds first room to queue
        if self.visited[start_x][start_y] == False:  # checks if current room has been visited
            queue.enqueue(self.maze.maze_array[start_x][start_y])
            self.visited[start_x][start_y] = True
            path_dict[self.maze.maze_array[start_x][start_y]] = None

        # performs BFS until any item is found or queue is empty
        while not self.found and queue.length > 0:
            curr = queue.dequeue().data
            if curr.item is not None:
                last = curr
                self.found = True

            if curr.x != 0 and self.visited[curr.x-1][curr.y] is False:  # has left neighbor
                queue.enqueue(self.maze.maze_array[curr.x-1][curr.y])
                self.visited[curr.x-1][curr.y] = True
                path_dict[self.maze.maze_array[curr.x-1][curr.y]] = curr

            if curr.x != self.maze.size-1 and self.visited[curr.x+1][curr.y] is False:  # has right neighbor
                queue.enqueue(self.maze.maze_array[curr.x+1][curr.y])
                self.visited[curr.x+1][curr.y] = True
                path_dict[self.maze.maze_array[curr.x+1][curr.y]] = curr

            if curr.y != 0 and self.visited[curr.x][curr.y-1] is False:  # has above neighbor
                queue.enqueue(self.maze.maze_array[curr.x][curr.y-1])
                self.visited[curr.x][curr.y-1] = True
                path_dict[self.maze.maze_array[curr.x][curr.y-1]] = curr

            if curr.y != self.maze.size-1 and self.visited[curr.x][curr.y+1] is False:  # has below neighbor
                queue.enqueue(self.maze.maze_array[curr.x][curr.y+1])
                self.visited[curr.x][curr.y+1] = True
                path_dict[self.maze.maze_array[curr.x][curr.y+1]] = curr

        # retrace path from last position to start
        path_list = []
        if self.found:
            while last is not None:
                path_list.append(path_dict.get(last))
                last = path_dict.get(last)

        return path_list

    def dfs(self, start_x, start_y):
        stack = Stack()
        last = None
        path_dict = {last: None}

        # adds first room to stack
        if self.visited[start_x][start_y] == False:  # checks if current room has been visited
            stack.push(self.maze.maze_array[start_x][start_y])
            self.visited[start_x][start_y] = True
            path_dict[self.maze.maze_array[start_x][start_y]] = None

        # performs DFS until any item is found or stack is empty
        while not self.found and stack.length > 0:
            curr = stack.pop()  # Room

            if curr.item is not None:
                last = curr  # Room
                self.found = True

            if curr.x != 0 and self.visited[curr.x-1][curr.y] is False:  # has left neighbor
                stack.push(self.maze.maze_array[curr.x-1][curr.y])
                self.visited[curr.x-1][curr.y] = True
                path_dict[self.maze.maze_array[curr.x-1][curr.y]] = curr

            if curr.x != self.maze.size-1 and self.visited[curr.x+1][curr.y] is False:  # has right neighbor
                stack.push(self.maze.maze_array[curr.x+1][curr.y])
                self.visited[curr.x+1][curr.y] = True
                path_dict[self.maze.maze_array[curr.x+1][curr.y]] = curr

            if curr.y != 0 and self.visited[curr.x][curr.y-1] is False:  # has above neighbor
                stack.push(self.maze.maze_array[curr.x][curr.y-1])
                self.visited[curr.x][curr.y-1] = True
                path_dict[self.maze.maze_array[curr.x][curr.y-1]] = curr

            if curr.y != self.maze.size-1 and self.visited[curr.x][curr.y+1] is False:  # has below neighbor
                stack.push(self.maze.maze_array[curr.x][curr.y+1])
                self.visited[curr.x][curr.y+1] = True
                path_dict[self.maze.maze_array[curr.x][curr.y+1]] = curr

        # retrace path from last position to start
        path_list = []
        if self.found:
            while last is not None:
                path_list.append(path_dict.get(last))
                last = path_dict.get(last)

        return path_list

    def dijkstra(self, start_x, start_y, target):
        pq = Heap()
        last = None
        path_dict = {last: None}
        heap_dict = {}
        mazearr = self.maze.maze_array

        # hashing Rooms to HeapData objects to keep track of indices
        for i in range(len(mazearr)):
            for j in range(len(mazearr[i])):
                heap_dict[mazearr[i][j]] = pq.insert(mazearr[i][j], np.inf)

        # decreasing key of starting position to 0
        pq.decrease_key(heap_dict[mazearr[start_x][start_y]], 0)
        curr = heap_dict[mazearr[start_x][start_y]]

        # perform dijkstra until target has been found or until heap is empty
        while curr != target and len(pq.heaplist) > 1:
            curr = pq.extract_min()  # HeapData
            last = curr.data  # Room

            if curr.data.x != 0:  # has left neighbor
                self.visited[curr.data.x-1][curr.data.y] = True
                if curr.key + mazearr[curr.data.x-1][curr.data.y].energy_cost < heap_dict.get(mazearr[curr.data.x-1][curr.data.y]).key:
                    heap_data = heap_dict.get(mazearr[curr.data.x-1][curr.data.y])
                    new_key = curr.key + mazearr[curr.data.x-1][curr.data.y].energy_cost
                    pq.decrease_key(heap_data, new_key)
                    path_dict[mazearr[curr.data.x-1][curr.data.y]] = curr.data

            if curr.data.x != self.maze.size-1:  # has right neighbor
                self.visited[curr.data.x+1][curr.data.y] = True
                if curr.key + mazearr[curr.data.x+1][curr.data.y].energy_cost < heap_dict.get(mazearr[curr.data.x+1][curr.data.y]).key:
                    heap_data = heap_dict.get(mazearr[curr.data.x+1][curr.data.y])
                    new_key = curr.key + mazearr[curr.data.x+1][curr.data.y].energy_cost
                    pq.decrease_key(heap_data, new_key)
                    path_dict[mazearr[curr.data.x+1][curr.data.y]] = curr.data

            if curr.data.y != 0:  # has above neighbor
                self.visited[curr.data.x][curr.data.y-1] = True
                if curr.key + mazearr[curr.data.x][curr.data.y-1].energy_cost < heap_dict.get(mazearr[curr.data.x][curr.data.y-1]).key:
                    heap_data = heap_dict.get(mazearr[curr.data.x][curr.data.y-1])
                    new_key = curr.key + mazearr[curr.data.x][curr.data.y-1].energy_cost
                    pq.decrease_key(heap_data, new_key)
                    path_dict[mazearr[curr.data.x][curr.data.y-1]] = curr.data

            if curr.data.y != self.maze.size-1:  # has below neighbor
                self.visited[curr.data.x][curr.data.y+1] = True
                if curr.key + mazearr[curr.data.x][curr.data.y + 1].energy_cost < heap_dict.get(mazearr[curr.data.x][curr.data.y+1]).key:
                    heap_data = heap_dict.get(mazearr[curr.data.x][curr.data.y + 1])
                    new_key = curr.key + mazearr[curr.data.x][curr.data.y + 1].energy_cost
                    pq.decrease_key(heap_data, new_key)
                    path_dict[mazearr[curr.data.x][curr.data.y+1]] = curr.data

        # retrace path from last position to start
        path_list = []
        path_dict[mazearr[start_x][start_y]] = None

        while last is not None:
            path_list.append(path_dict.get(last))
            last = path_dict.get(last)

        return path_list


if __name__ == '__main__':
    m = Maze(100)
    print(m)
    probe = Probe(3, m)
    print(probe.dijkstra(0, 0, 0))


