# Is not advisable to use list with stack
# use deque instead.
# Inserting in queue,we use appendLeft.

import threading
from collections import deque
import time

class Queue:
    def __init__(self):
        self.buffer=deque()
    # insertion
    def enqueue(self,val):
        self.buffer.appendleft(val)
    # deletion
    def dequeue(self):
       return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

queue = Queue()

def place_Order(list):
    for order in list:
        print('ordering for :',order)
        queue.enqueue(order)
        time.sleep(0.5)


def server_Order():
    time.sleep(1)
    while not queue.is_empty():
      order=queue.dequeue()
      print('we serving you :',order)
      time.sleep(2)
      mylist=list()





if __name__ == '__main__':
    Orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    #creating thread 1
    t1=threading.Thread(target=place_Order, args=(Orders,))
    #creating thread 2
    t2=threading.Thread(target=server_Order)
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

# telling the main thread to wait until both threads are completely executed
    t1.join()
    t2.join()
    print('jude')

    print('done!!')

