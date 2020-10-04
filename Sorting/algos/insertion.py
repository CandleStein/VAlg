import matplotlib.pyplot as plt
import numpy as np


def insertionsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0) and (temp < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
        plt.stem(arr)
        plt.pause(1e-8)
        plt.clf()
    return arr


if __name__ == "__main__":
    arr = np.random.randint(0, 100, 100)
    arr = insertionsort(arr)
    plt.stem(arr)
    plt.show()
