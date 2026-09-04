import random

def BubbleSort(arr):

    for i in range(len(arr)):
        j = i + 1
        while j < len(arr) - 1:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
    print(arr)

new_list = [0, 9, 10, 2, 3, 4]

BubbleSort(new_list)