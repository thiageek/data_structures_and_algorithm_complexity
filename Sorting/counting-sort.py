#!/bin/python3
import time

filepath = 'data.txt'

def counting_sort(data):
    k = max(data)+1
    aux = [0] * k
    output = [0] * len(data)
    
    for i in range(0, len(data)):
        aux[data[i]] += 1
    
    for i in range(1, k):
        aux[i] += aux[i-1]

    for i in range(len(data)-1, -1, -1):
        output[aux[data[i]]-1] = data[i]
        aux[data[i]] -= 1
        
    return output

if __name__ == '__main__':
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        arr = [int(num) for num in line.split()]
        print("#####"*(len(arr)+2))
        print("Input:  ", arr)
        start_time = time.time()
        print("Output: ", counting_sort(arr))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")
