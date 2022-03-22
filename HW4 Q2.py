import time
import numpy as np
import matplotlib.pyplot as plt

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr,l,r):
    if l < r:
        m = l + (r-l)//2
        if m<=5000:
          mergeSort(arr, l, m)
          mergeSort(arr, m+1, r)
          merge(arr, l, m, r)
        else:
          insertionSort(arr)

sorts = [
    {
        "name": "Insertion Sort",
        "sort": lambda arr: insertionSort(arr)
    },
    {
        "name": "Merge Sort",
        "sort": lambda arr: mergeSort(arr, 0, len(arr) - 1)
    }
]

elements = np.array([i*1 for i in range(1, 500)])

plt.xlabel('List Length')
plt.ylabel('Time Complexity')

for sort in sorts:
    times = list()
    start_all = time.clock()
    for i in range(1, 500):
        start = time.clock()
        a = np.random.randint(10, size = i * 1)
        sort["sort"](a)
        end = time.clock()
        times.append(end - start)
    end_all = time.clock()
    plt.plot(elements, times, label = sort["name"])

plt.grid()
plt.legend()
plt.show()
