class HeapData:
    def __init__(self, data, key, index):
        self.data = data
        self.key = key
        self.index = index

    def __str__(self):
        return "(" + str(self.data) + ", " + str(self.key) + ")"


class Heap:
    def __init__(self):
        self.heaplist = []
        self.num_elements = 0

    def __str__(self):
        result = ""
        for i in range(0, self.num_elements):
            result += str(self.heaplist[i]) + " "
        return result

    def swap(self, first, second):
        temp = self.heaplist[first.index]
        self.heaplist[first.index] = second
        self.heaplist[second.index] = temp

        temp = first.index
        first.index = second.index
        second.index = temp

    def left(self, heap_data):
        index = heap_data.index
        if ((2*index) + 1) >= self.num_elements:
            return None
        else:
            return self.heaplist[(2*index) + 1]

    def right(self, heap_data):
        index = heap_data.index
        if ((2*index) + 2) >= self.num_elements:
            return None
        else:
            return self.heaplist[(2*index) + 2]

    def parent(self, heap_data):
        index = heap_data.index
        return self.heaplist[(index-1) // 2]

    def insert(self, data, key):
        heap_data = HeapData(data, key, self.num_elements)
        self.heaplist.append(heap_data)
        self.num_elements += 1
        self.decrease_key(heap_data, key)
        return heap_data

    def decrease_key(self, heap_data, new_key):
        heap_data.key = new_key
        index = heap_data.index

        while index > 0 and self.heaplist[self.parent(heap_data).index].key > heap_data.key:
            self.swap(self.heaplist[index], self.parent(self.heaplist[index]))
            index = self.parent(self.heaplist[index]).index

    def extract_min(self):
        self.swap(self.heaplist[0], self.heaplist[self.num_elements-1])
        min = self.heaplist[self.num_elements-1]
        self.heaplist.pop(self.num_elements-1)
        self.num_elements -= 1
        self.heapify(self.heaplist[0])
        return min

    def heapify(self, heap_data):
        if heap_data is not None:
            if self.left(heap_data) is not None:
                if self.right(heap_data) is not None:  # if two children
                    # checks heap property
                    if heap_data.key > self.left(heap_data).key or heap_data.key > self.right(heap_data).key:
                        if self.left(heap_data).key < self.right(heap_data).key:
                            self.swap(heap_data, self.left(heap_data))
                        else:
                            self.swap(heap_data, self.right(heap_data))
                        self.heapify(heap_data)
                else:  # if only left child
                    if heap_data.key > self.left(heap_data).key:
                        self.swap(heap_data, self.left(heap_data))


if __name__ == '__main__':
    h = Heap()
