import threading
import os

def task1():
    print ('task1 is assigned to :{}'.format(threading.current_thread().name))
    print('the ID of processing running task1 :{}'.format(os.getpid()))

def task2():
    print('task2 is assigned to :{}'.format(threading.current_thread().name))
    print('the ID of processing running task2 : {}'.format(os.getpid()))


if __name__ == '__main__':
 print('main thread is assigned to :{}'.format(threading.main_thread().name))
 print('the ID of processing running main thread : {}'.format(os.getpid()))

 # creating thread
 t1=threading.Thread(target=task1)
 t2=threading.Thread(target=task2)

 # starting thread
 t1.start()
 t2.start()

 # wait until thread 1 is completely executed
 t1.join()
 # wait until thread 2 is completely executed
 t2.join()

 # when both threads are completely executed
 print('Done!')














