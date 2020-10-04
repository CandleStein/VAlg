import numpy as np
import matplotlib.pyplot as plt


def merge(arr, start, mid, end):
    temp_arr = np.array(arr)
    i = start
    j = mid
    k = start
    while i < mid and j < end and k < end:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i = i + 1
        else:
            temp_arr[k] = arr[j]
            j = j + 1
        k += 1
    while i < mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j < end:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    return temp_arr


def mergesort(arr, start, end):
    if (end - start) <= 1:
        return arr
    mid = (start + end) // 2
    arr = mergesort(arr, start, mid)
    arr = mergesort(arr, mid, end)
    arr = merge(arr, start, mid, end)
    plt.stem(arr)
    plt.pause(0.0001)
    plt.clf()
    return arr


def msort(arr):
    return mergesort(arr, 0, len(arr))


if __name__ == "__main__":
    arr = np.random.randint(0, 1000, 100)
    arr = mergesort(arr, 0, len(arr))
    plt.stem(arr)
    plt.show()
