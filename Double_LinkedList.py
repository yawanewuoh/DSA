class Node:
    def __init__(self, data=None, next=None,prev=None):
        self.data = data
        self.next = next
        self.prev=prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail= None

    def print_backwards(self):
        # If LinkedList is empty and inserting at first.
        if self.head is None:
            print("Empty LinkedList")
        else:
            # printing from backwards(tail)
            itr=self.tail
            linked_string = ''
            while itr:
                linked_string+=str(itr.data)+" -->"
                itr=itr.prev
            print(linked_string)

    def print_forward(self):
        # If LinkedList is empty and inserting at first.
        if self.head is None:
            print("Empty LinkedList")
        else:
            # printing towards the end(from head)
            itr = self.head
            linked_string = ''
            while itr:
                linked_string += str(itr.data) + " -->"
                itr = itr.next
            print(linked_string)



    def insert_at_end(self,data):
        # If LinkedList is empty and inserting at first.
     if self.head is None:
         self.head=Node(data)
     else:
         # Every new node inserted must inherit  the tail
         itr=self.head
         while itr.next:
             itr = itr.next
         itr.next=Node(data)
         self.tail=itr.next
         self.tail.prev=itr


if __name__ == '__main__':
 dl=DoubleLinkedList()
 dl.insert_at_end(10)
 dl.insert_at_end(20)
 dl.insert_at_end(40)
 dl.insert_at_end(50)
 # dl.print_forward()
 dl.print_backwards()







