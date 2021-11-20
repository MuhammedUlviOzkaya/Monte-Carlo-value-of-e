from ulvi import ValueE
from threading import Thread
import os

n = 1000000


n_values = []

"""value e class objects"""
value_es = []

threads = []

for i in range(os.cpu_count()):
    value_es.append(ValueE())
    threads.append(Thread(target=value_es[i].n_values, args=(n,)))

for thread in threads:
    thread.start()
    print("Started thread number %d" % threads.index(thread))

for thread in threads:
    thread.join()


for value_e in value_es:
    for es in value_e.n_array:
        n_values.append(es)

def average(array):
    total = 0
    for i in array:
        total += i
    return total / len(array)

e = average(n_values)

print(e)




