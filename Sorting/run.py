from algos import bubble, insertion, merge, quick, radix, selection
import argparse
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description="Sorting Visualisation")
parser.add_argument(
    "-a",
    "--algorithm",
    choices=["bubble", "insertion", "merge", "quick", "radix", "selection"],
    default="quick",
    help="The sorting algorithm to follow",
)
args = parser.parse_args()
mode = args.algorithm

funcs = [
    bubble.bubblesort,
    insertion.insertionsort,
    merge.msort,
    quick.qsort,
    radix.radixsort,
    selection.selectionsort,
]
ids = ["bubble", "insertion", "merge", "quick", "radix", "selection"]
map_ = {i: f for f, i in zip(funcs, ids)}

if __name__ == "__main__":
    f = map_[mode]
    arr = np.random.randint(0, 100, 100)
    arr = f(arr)
    plt.stem(arr)
    plt.show()
