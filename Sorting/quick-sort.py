#!/bin/python3
import time

filepath = 'data.txt'

def quick_sort(data, low, high):
    if(low < high):
        pivot = partition(data, low, high)
        quick_sort(data, low, pivot -1)
        quick_sort(data, pivot + 1, high)
    return data

def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if(data[j] <= pivot):
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[high] = data[high], data[i+1]
    return i+1

if __name__ == '__main__':
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        arr = [int(num) for num in line.split()]
        print("#####"*(len(arr)+2))
        print("Input:  ", arr)
        start_time = time.time()
        print("Output: ", quick_sort(arr, 0, len(arr)-1))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")
