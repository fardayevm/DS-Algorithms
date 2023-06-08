class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            # when new value already exists in the tree
            if new_node.value == temp.value:
                return False
            # when new value is less than the root value
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # when new value is more than the root value
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
    def contains(self, value):
        # no need to the following two lines of code
        # if self        .root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            elif value == temp.value:
                return True
        return False

        

my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(53)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(15))
