from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.queue_list = DoublyLinkedList()
        self.length = 0

    def __str__(self):
        return str(self.queue_list)

    def enqueue(self, data):
        self.queue_list.append(data)
        self.length += 1

    def dequeue(self):
        head = self.queue_list.head
        self.queue_list.behead()
        self.length -= 1
        return head

    def is_empty(self):
        if self.length <= 0:
            return True
        else:
            return False

    def get_top(self):
        return self.queue_list.head


if __name__ == "__main__":
    q = Queue()

