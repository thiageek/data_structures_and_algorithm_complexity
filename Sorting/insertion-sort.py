#!/bin/python3
import time

filepath = 'data.txt'

def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if(data[j] < data[j-1]):
                data[j], data[j-1] = data[j-1], data[j]
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
        print("Output: ", insertion_sort(arr))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")