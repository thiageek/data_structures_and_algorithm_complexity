#!/bin/python3
import time

filepath = 'data.txt'

def selection_sort(data):
    for i in range(len(data)):
        min = i
        for j in range(i+1, len(data)):
            if(data[j] < data[min]):
                min = j
        if(i != min):
            data[i], data[min] = data[min], data[i]
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
        print("Output: ", selection_sort(arr))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")
