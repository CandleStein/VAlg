import numpy as np
import matplotlib.pyplot as plt


def selectionsort(arr):
    for i in range(len(arr)):
        mid = i
        for j in range(i + 1, len(arr)):
            if arr[mid] > arr[j]:
                mid = j
        arr[i], arr[mid] = arr[mid], arr[i]  # swap
        plt.stem(arr)
        plt.pause(1e-4)
        plt.clf()
    return arr


if __name__ == "__main__":
    arr = np.random.randint(0, 100, 100)
    arr = selectionsort(arr)
    plt.stem(arr)
    plt.show()
