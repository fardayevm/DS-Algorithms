class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True

    def pop(self):

        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # when started with zero item
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # when started with one item
        if self.length == 0:
            self.tail = None
        return temp
    
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None 
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        # adding to the beginning
        if index == 0:
            return self.prepend(value)
        # adding to the end
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get_value(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def addTwoNumbers(self,l1,l2):

        def reverse_ll(list):
            temp = self.head
            before = None
            while temp:
                next_node = temp.next
                temp.next = before
                before = temp
                temp = next_node
            self.head = before
        
        list1 = []
        list2 = []
        num1 = reverse_ll(l1)
        num2 = reverse_ll(l2)
        
            
           


# 243 564
my_list = LinkedList(2)
my_list.append(4)
my_list.append(3)

my_list2 =  LinkedList(5)
my_list.append(6)
my_list.append(4)
