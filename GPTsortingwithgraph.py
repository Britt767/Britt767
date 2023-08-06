# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:36:05 2023

@author: byer7
"""

import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def generate_random_array(size):
    arr = [random.randint(1, size) for _ in range(size)]
    return arr

def measure_sorting_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def compare_sorting_algorithms(array_sizes):
    bubble_sort_times = []
    selection_sort_times = []
    insertion_sort_times = []

    for size in array_sizes:
        arr = generate_random_array(size)

        bubble_sort_time = measure_sorting_time(bubble_sort, arr[:])
        bubble_sort_times.append(bubble_sort_time)

        selection_sort_time = measure_sorting_time(selection_sort, arr[:])
        selection_sort_times.append(selection_sort_time)

        insertion_sort_time = measure_sorting_time(insertion_sort, arr[:])
        insertion_sort_times.append(insertion_sort_time)

    plt.plot(array_sizes, bubble_sort_times, label='Bubble Sort')
    plt.plot(array_sizes, selection_sort_times, label='Selection Sort')
    plt.plot(array_sizes, insertion_sort_times, label='Insertion Sort')

    plt.xlabel('Array Size')
    plt.ylabel('Sorting Time (seconds)')
    plt.title("Brian's Algorithm Comparison")
    plt.legend()
    plt.show()

# Set the array sizes for comparison
array_sizes = [100, 500, 1000, 2000, 3000]

# Compare the sorting algorithms and plot the graph
compare_sorting_algorithms(array_sizes)
