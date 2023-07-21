class Stack:
    def __init__(self):
        self.max_size = 50
        self.stack_list = [] * self.max_size
        self.length = 0

    def __str__(self):
        return str(self.stack_list)

    def push(self, data):
        self.stack_list.append(data)
        self.length += 1

    def pop(self):
        top = self.stack_list[self.length-1]
        self.stack_list.remove(self.stack_list[self.length-1])
        self.length -= 1
        return top

    def is_empty(self):
        if self.length <= 0:
            return True
        else:
            return False

    def is_full(self):
        if self.length >= self.max_size:
            return True
        else:
            return False

    def get_top(self):
        return self.stack_list[self.length-1]


if __name__ == "__main__":
    s = Stack()

