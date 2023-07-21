class Player:
    def __init__(self):
        self.energy = 100
        self.inventory = []

    def __str__(self):
        return ("A player with " + str(self.energy) +
                " energy and an inventory containing: " + self.display_inventory())

    def display_inventory(self):
        result = "["
        for i in range(len(self.inventory)):
            if i > 0:
                result += ", "
            result += str(self.inventory[i])
        result += "]"
        return result

    def add_to_inventory(self, item):
        self.inventory.append(item)


if __name__ == '__main__':
    p = Player()
