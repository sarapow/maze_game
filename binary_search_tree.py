class TreeNode:
    def __init__(self, data, left, right, parent):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data) + ' '


def swap(first, second):
    temp = first.data
    first.data = second.data
    second.data = temp


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.in_order_walk(self.root)

    def in_order_walk(self, subroot):
        result = ""
        if subroot is not None:
            result += self.in_order_walk(subroot.left) + ' '
            result += str(subroot.data)
            result += ' ' + self.in_order_walk(subroot.right)
        return result

    def search_for_node(self, subroot, data):
        if subroot is not None:
            if data == subroot.data:
                return subroot
            elif data < subroot.data:
                return self.search_for_node(subroot.left, data)
            else:
                return self.search_for_node(subroot.right, data)
        else:
            return None

    def insert_node(self, subroot, new_node):
        if subroot is not None:
            if new_node.data < subroot.data:
                if subroot.left is None:
                    subroot.left = new_node
                    new_node.parent = subroot
                else:
                    self.insert_node(subroot.left, new_node)
            else:
                if subroot.right is None:
                    subroot.right = new_node
                    new_node.parent = subroot
                else:
                    self.insert_node(subroot.right, new_node)

    def insert(self, data):
        new_node = TreeNode(data, None, None, None)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    def find_min(self, subroot):
        if subroot is not None:
            if subroot.left is None:
                return subroot
            else:
                return self.find_min(subroot.left)

    def find_max(self, subroot):
        if subroot is not None:
            if subroot.right is None:
                return subroot
            else:
                return self.find_max(subroot.right)

    def delete(self, subroot, data):
        if subroot is not None:
            # left subtree
            if data < subroot.data:
                subroot.left = self.delete(subroot.left, data)

            # right subtree
            elif data > subroot.data:
                subroot.right = self.delete(subroot.right, data)

            # node to delete
            else:
                # one or no children
                if subroot.left is None:
                    temp = subroot.right
                    subroot = None
                    return temp
                elif subroot.right is None:
                    temp = subroot.left
                    subroot = None
                    return temp

                # two children
                temp = self.find_min(subroot.right)

                # copy successor
                subroot.data = temp.data

                # delete successor
                subroot.right = self.delete(subroot.right, temp.data)
        return subroot


if __name__ == "__main__":
    tree = BinarySearchTree()



