#!/bin/python3
import time

filepath = 'data.txt'

def max_heapify(data, i=0):
    left = (2 * i) + 1
    right = (2 * i) + 2
    greater = i

    if(left < len(data) and data[left] > data[i]):
        greater = left
    
    if(right < len(data) and data[right] > data[greater]):
        greater = right
    
    if(greater != i):
        data[i], data[greater] = data[greater], data[i]
        data = max_heapify(data, i=greater)

    return data

if __name__ == '__main__':
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        arr = [int(num) for num in line.split()]
        print("#####"*(len(arr)+2))
        print("Input:  ", arr)
        start_time = time.time()
        print("Output: ", max_heapify(arr))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")
