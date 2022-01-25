import threading
import time
from random import randint


histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        make_histogram(self.counter, 0.01)
        print("Exiting " + self.name)


def make_histogram(counter, delay):
    while counter:
        time.sleep(delay)
        num = (randint(0,100))
        for i in range(1,10):
            if num <= i*10:
                histogram[i-1] += 1
                break
            else:
                continue
        print(histogram)
        counter -= 1


thread1 = myThread(1, "Thread-1", 50)
thread2 = myThread(2, "Thread-2", 50)

thread1.start()
thread2.start()



