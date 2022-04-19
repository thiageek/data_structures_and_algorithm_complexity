#!/bin/python3
import time

filepath = 'data.txt'

def radix_sort(data):
    d = len(str(max(data)))
    
    for i in range(d-1, -1, -1):
        aux = [[] for n in range(10)]
        for j in range(0, len(data)):
            value = str(data[j]).zfill(d)
            aux[int(value[i])].append(data[j])
        data = sum((k for k in aux), [])

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
        print("Output: ", radix_sort(arr))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")
