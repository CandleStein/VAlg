import numpy as np
import matplotlib.pyplot as plt


def countingsort(arr, exp):
    n = len(arr)
    output = [0] * len(arr)
    count = [0] * 10
    for i in range(0, n):
        idx = int(arr[i] / exp) % 10
        count[idx] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
        i = n - 1
    while i >= 0:
        idx = int((arr[i] / exp) % 10)
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
        i -= 1
    return output


def radixsort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 1:
        arr = countingsort(arr, exp)
        exp *= 10
        plt.stem(arr)
        plt.pause(1e-3)
        plt.clf()
    return arr


if __name__ == "__main__":
    arr = np.random.randint(0, 10000, 100)
    arr = radixsort(arr)
    plt.stem(arr)
    plt.show()
