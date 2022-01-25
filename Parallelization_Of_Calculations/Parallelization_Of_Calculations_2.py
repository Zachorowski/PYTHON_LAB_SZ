import threading
import time

start = time.perf_counter()
fork =[0,1,1,1,1,1]

class Philospher(threading.Thread):
    def __init__(self, threadID, name, hunger):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.hunger = hunger

    def run(self):
        print("Je " + self.name)
        self.eat()
        print(self.name + " skończył jeść\n")


    def eat(self):
        if ((fork[self.threadID-1] and fork[self.threadID]) == 1):
            fork[self.threadID] = 0
            fork[self.threadID-1] = 0
            time.sleep(0.1)
            self.hunger -= 1
            fork[self.threadID] = 1
            fork[self.threadID + 1] = 1

thread1 = Philospher(1, "Arystoteles", 10)
thread2 = Philospher(2, "Platon", 10)
thread3 = Philospher(3, "Kierkegaard", 10)
thread4 = Philospher(4, "Heidegger", 10)
thread5 = Philospher(5, "Nietzsche", 10)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

finish = time.perf_counter()
print(f'Skończyli jeść w {round(finish-start, 3)} sekund')