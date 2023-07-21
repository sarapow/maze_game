class Node:

    def __init__(self, data, prev_node, next_node):
        self.data = data
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return str(self.data)


def swap(node1, node2):
    temp = node1.data
    node1.data = node2.data
    node2.data = temp


def merge(list1, list2):
    curr1 = list1.tail
    curr2 = list2.tail
    result = DoublyLinkedList()

    while curr1 is not None and curr2 is not None:
        if curr1.data > curr2.data:
            result.add_to_head(curr1.data)
            curr1 = curr1.prev
        else:
            result.add_to_head(curr2.data)
            curr2 = curr2.prev

    while curr1 is not None:
        result.add_to_head(curr1.data)
        curr1 = curr1.prev

    while curr2 is not None:
        result.add_to_head(curr2.data)
        curr2 = curr2.prev

    return result


def partition(start, end):
    first_UK = start
    last_LHS = start.prev
    pivot = end
    curr = start

    while curr != end:
        if first_UK is not None and pivot is not None:
            if first_UK.data < pivot.data:
                if last_LHS is None:  # on first comparison
                    last_LHS = start
                    swap(first_UK, last_LHS)
                else:
                    swap(first_UK, last_LHS.next)
                    last_LHS = last_LHS.next
                first_UK = first_UK.next
            else:
                first_UK = first_UK.next
            curr = curr.next

    if last_LHS is None:
        swap(pivot, start)
        return start
    else:
        swap(pivot, last_LHS.next)
        return last_LHS.next  # pivot


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = ""
        curr = self.head

        while curr is not None:
            result += str(curr.data) + " "
            curr = curr.next

        return result

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def find_length(self):
        curr = self.head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.next

        return count

    def get_mid(self):
        curr = self.head

        for i in range((self.find_length() + 1) // 2):
            if curr is not None:
                curr = curr.next

        return curr

    def add_to_head(self, data):
        new_node = Node(data, None, self.head)

        # if list is empty
        if self.head is None:
            self.tail = new_node  # head and tail point to same
        else:
            self.head.prev = new_node

        self.head = new_node

    def append(self, data):
        new_node = Node(data, self.tail, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def search_for_node(self, data):
        curr = self.head

        while curr is not None and curr.data != data:
            curr = curr.next

        return curr

    def delete(self, data):
        to_delete = self.search_for_node(data)
        predecessor = to_delete.prev
        successor = to_delete.next

        if to_delete is not None:
            if predecessor is None:
                if successor is None:  # empty list
                    self.head = None
                    self.tail = None
                else:  # to_delete is head
                    successor.prev = None
                    self.head = successor
            elif successor is None:
                if predecessor is not None:  # if to_delete is tail
                    predecessor.next = None
                    self.tail = predecessor
            else:  # if to_delete is in mid
                predecessor.next = successor
                successor.prev = predecessor

    def behead(self):
        if self.head is not None:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def sel_sort(self):
        compare = self.head

        while compare is not None:
            min_val = compare
            curr = self.head
            while curr is not None:
                if curr.data > min_val.data:
                    swap(curr, min_val)
                curr = curr.next
            compare = compare.next

    def in_sort(self):
        forward = self.head.next

        while forward is not None:
            back = forward.prev

            while back is not None and back.next.data < back.data:
                swap(back.next, back)
                back = back.prev

            forward = forward.next

    def split_list(self):
        curr = self.tail  # walk backwards to use add_to_head()
        left = DoublyLinkedList()
        right = DoublyLinkedList()

        if curr is not None:
            while curr is not self.get_mid().prev:
                right.add_to_head(curr.data)
                curr = curr.prev
            while curr is not None:
                left.add_to_head(curr.data)
                curr = curr.prev

        return left, right

    def merge_sort(self):
        if self.find_length() > 1:
            left, right = self.split_list()

            left_result = left.merge_sort()
            right_result = right.merge_sort()

            return merge(left_result, right_result)
        else:
            return self

    def quick_sort(self, start, end):
        if start is not None and end is not None:
            if start != end and start != end.next:
                pivot = partition(start, end)

                if pivot.prev is not None:
                    self.quick_sort(start, pivot.prev)
                if pivot.next is not None:
                    self.quick_sort(pivot.next, end)


if __name__ == '__main__':
    dl = DoublyLinkedList()