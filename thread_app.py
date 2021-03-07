import threading
import time

myLock = threading.Lock()


def display_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("{} {}\n".format(threadName, time.ctime(time.time())))
        counter -= 1


class myThread(threading.Thread):
    def __init__(self, threadid, name, count):
        threading.Thread.__init__(self)
        self.threadid = threadid
        self.name = name
        self.count = count

    def run(self):
        print("Starting {} with Id: {}".format(self.name, self.threadid))
        myLock.acquire()
        display_time(self.name, self.count, 5)
        myLock.release()


thread1 = myThread(1, "thread-1", 2)
thread2 = myThread(2, "thread-2", 3)

thread1.start()
thread2.start()
