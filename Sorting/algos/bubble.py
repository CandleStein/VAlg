import numpy as np
import matplotlib.pyplot as plt


def bubblesort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            plt.stem(arr)
            plt.pause(1e-10)
            plt.clf()
    return arr


if __name__ == "__main__":
    arr = np.random.randint(0, 100, 20)
    arr = bubblesort(arr)
    plt.stem(arr)
    plt.show()
