import numpy as np
import matplotlib.pyplot as plt


def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(arr, start, end):
    if len(arr) == 1:
        return arr
    if start < end:
        pi = partition(arr, start, end)
        quicksort(arr, start, pi - 1)
        quicksort(arr, pi + 1, end)
    plt.stem(arr)
    plt.pause(0.0001)
    plt.clf()
    return arr


def qsort(arr):
    return quicksort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = np.random.randint(0, 100, 100)
    quicksort(arr, 0, len(arr) - 1)
    plt.stem(arr)
    plt.show()
