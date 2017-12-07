import timeit
import random
import seaborn as sns
import numpy as np

# sorts written by Jim Fix
# https://jimfix.github.io/csci121/index.html
def insertion_sort(xs):
    i = 1
    while i < len(xs):
        # place xs[i] properly into sorted xs[:i] using a series of swaps
        j = i - 1
        while j >= 0 and xs[j] > xs[j+1]:
            xs[j],xs[j+1] = xs[j+1],xs[j]
            j -= 1
        i += 1

def bubble_sort(xs):
    i = 0
    while i < len(xs)-1:
        # bubble lighter values to the left
        j = len(xs) - 2
        while j >= i:
            if xs[j+1] < xs[j]:
                xs[j],xs[j+1] = xs[j+1],xs[j]
            j -= 1
        i += 1

def partition(xs, first, last):
    pivot, pivot_value = first, xs[first]
    i = first + 1
    while i <= last:
        if xs[i] <= pivot_value:
            xs[pivot+1],xs[i] = xs[i],xs[pivot+1]
            pivot = pivot + 1
        i += 1
    xs[first],xs[pivot] = xs[pivot],xs[first]
    return pivot

def quicksort_helper(xs, left, right):
    if left < right: 
        pivot = partition(xs, left, right)
        quicksort_helper(xs, left, pivot - 1)
        quicksort_helper(xs, pivot + 1, right)

def quicksort(xs):  
    quicksort_helper(xs, 0, len(xs)-1)

def mergesort(xs):
    if len(xs) > 1:
        middle = len(xs) // 2
        lefts  = xs[:middle]
        rights = xs[middle:]
        mergesort(lefts)
        mergesort(rights)
        merge(lefts,rights,xs)

def merge(ls,rs,xs):
    xi, li, ri = 0, 0, 0
    while xi < len(xs):
        l_valid, r_valid = li < len(ls), ri < len(rs)
        if l_valid and ((not r_valid) or ls[li] <= rs[ri]):
            xs[xi] = ls[li]
            li += 1
        else:
            xs[xi] = rs[ri]
            ri += 1
        xi += 1

def randList(n):
    randomList = random.sample(range(0,n), n)
    return randomList

def manyLists(n, l):
    randomLists = [ randList(l) for x in range(l) ]
    return randomLists

sizes = []
times = []
quickTimes = []
for x in range (0, 100):
    testLists = manyLists(10, x)
    mergeTime = timeit.timeit('[ mergesort(l) for l in testLists ]', setup='from __main__ import testLists, mergesort, merge', number=1)
    quickTime = timeit.timeit('[ quicksort(l) for l in testLists ]', setup='from __main__ import testLists, quicksort, quicksort_helper, partition', number=1)
    # bubbleTime = timeit.timeit('[ bubble_sort(l) for l in testLists ]', setup='from __main__ import bubble_sort, testLists', number=1)
    # insertionTime = timeit.timeit('[ insertion_sort(l) for l in testLists ]', setup='from __main__ import insertion_sort, testLists', number=1)
    sizes.append(x)
    times.append(mergeTime)
    quickTimes.append(quickTime)
    print(x)

print('plotting')
sns.set()

# Load the example tips dataset
iris = sns.load_dataset("iris")

# Plot tip as a function of toal bill across days
g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species",
               truncate=True, size=5, data=iris)

# Use more informative axis labels than are provided by default
g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
