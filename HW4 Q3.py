#REF: https://stackoverflow.com/questions/63699687/why-does-the-hash-function-in-python-take-constant-time-to-operate-on-strings
import random
import time
import pylab

def form_str(k, n):
    for i in range(n):
        random_str = ''
        for j in range(k):
            nextchar = random.choice('abcdefghijklmnopqrstuvwxyz')
            random_str += nextchar
        yield random_str

def time_hash(k, n):
    total_time = 0.0
    for element in form_str(k, n):
        start_time = time.time()
        for i in range(100000):
            hash(element)
        end_time = time.time()
        total_time += (end_time - start_time)
    return round(total_time, 2)
 

def plot_time():
    x_values, y_values = [], []
    for k in range(0, 100000, 5000):
        x_values.append(k)
        y_values.append(time_hash(k, 100))
    # print(y_values)
    pylab.figure(1)
    pylab.title('Hash Map Complexity')
    pylab.xlabel('List Length')
    pylab.ylabel('Time Complexity')
    pylab.plot(x_values, y_values, 'r:', label = 'Hash time')
    pylab.show()

plot_time()
