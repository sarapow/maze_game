import random


class Room:
    def __init__(self, energy_cost, item, x, y):
        self.energy_cost = energy_cost
        self.item = item
        self.x = x
        self.y = y

    def __str__(self):
        s = "" + str(self.energy_cost) + " " + "(" + str(self.x) + "," + str(self.y) + ") " + "Item: " + str(self.item)
        return s


class Maze:
    def __init__(self, size):
        self.size = size
        self.exit = [self.size-1, self.size-1]
        self.maze_array = [None] * self.size

        for i in range(self.size):
            self.maze_array[i] = [None] * self.size
            for j in range(self.size):
                item = None
                rand = random.randint(1, 20)
                if rand > 19:
                    item = "Treasure"
                if rand == 18:
                    item = "Probe"
                self.maze_array[i][j] = Room(rand//2, item, i, j)

    def __str__(self):
        result = ""
        for i in range(self.size):
            result += "["
            for j in range(self.size):
                result += str(self.maze_array[i][j])
                result += " | "
            result += "] \n\n"

        return result


if __name__ == '__main__':
    maze = Maze(100)
    print(maze)





