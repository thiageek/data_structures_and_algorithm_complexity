#!/bin/python3
import time

filepath = 'data.txt'

def max_heapify(data, root=0):
    left = (2 * root) + 1
    right = (2 * root) + 2
    greater = root

    if(left < len(data) and data[left] > data[root]):
        greater = left
    
    if(right < len(data) and data[right] > data[greater]):
        greater = right
    
    if(greater != root):
        data[root], data[greater] = data[greater], data[root]
        max_heapify(data, root=greater)

    return data

def build_max_heap(data):
    heapSize = int(len(data) / 2)
    for i in range(heapSize, 0, -1):
        max_heapify(data, root=i-1)
    return data

def heap_sort(data):
    build_max_heap(data)
    newData = []
    for i in range(len(data)-1, -1, -1):
        newData.insert(0,data[0])
        data[0] = data[i]
        data = data[:len(data)-1]
        max_heapify(data)
    return newData

if __name__ == '__main__':
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        arr = [int(num) for num in line.split()]
        print("#####"*(len(arr)+2))
        print("Input:  ", arr)
        start_time = time.time()
        print("Output: ", heap_sort(arr))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")
