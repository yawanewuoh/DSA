class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data)

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            itr = self.head
            linked_string = ''
            while itr:
                linked_string += str(itr.data) + '-->'
                itr = itr.next
            print(linked_string)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        if self.head is None:
            print(0)
        else:
            count = 0
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            print(count)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("my_Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        itr = self.head
        node = Node(data)
        count = 0
        while itr:
            if count == index - 1:
                temp = itr.next
                itr.next = node
                node.next = temp
            itr = itr.next
            count += 1

    def insert_after_value(self, after_value, value_to_insert):
        itr = self.head
        node = Node(value_to_insert)
        while itr:
            if itr.data == after_value:
                temp = itr.next
                itr.next = node
                node.next = temp
            itr = itr.next

    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            itr = self.head
            previous = Node
            while itr.data is not data:
                previous = itr
                itr = itr.next
            temp = previous.next.next
            previous.next = temp



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.print()
    ll.insert_after_value('mango','apple')
    ll.print()
