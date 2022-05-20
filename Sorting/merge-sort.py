#!/bin/python3
import time

filepath = 'data.txt'

def merge_sort(data):
    if(len(data) > 1):
        mid = len(data) // 2

        left = data[:mid]
        right = data[mid:]
        
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if(left[i] <= right[j]):
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
        
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
        print("Output: ", merge_sort(arr))
        end_time = time.time()
        print("Executed in {:.10f} seconds".format(end_time - start_time))
        print("#####"*(len(arr)+2))
        print("\n")
