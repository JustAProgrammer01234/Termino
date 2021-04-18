'''
All non courotine objects are here.
'''
import time

def get_help():
    with open('txt files/help.txt','r') as f:
        return f.read()

def get_token():
    with open('txt files/token.txt','r') as f:
        return f.read()

def str_to_array(string):
    return [int(digit) for digit in string if digit.isdigit()]

def bubble_sort_ascending(array):
    index = 1
    for _ in range(len(array) - index):
        for i in range(len(array) - index):
            time.sleep(0.001)
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

def bubble_sort_descending(array):
    index = 1
    for _ in range(len(array) - index):
        for i in range(len(array) - index):
            time.sleep(0.001)
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

def insertion_sort_ascending(array):
    for i in range(1, len(array)):
        char = array[i]
        index = i - 1
        while index >= 0 and char < array[index]:
            array[index + 1] = array[index]
            index -= 1
            time.sleep(0.001)
        array[index + 1] = char
        time.sleep(0.001)

def insertion_sort_descending(array):
    for i in range(1, len(array)):
        char = array[i]
        index = i - 1
        while index >= 0 and char > array[index]:
            array[index + 1] = array[index]
            index -= 1
            time.sleep(0.001)
        array[index + 1] = char
        time.sleep(0.001)

def run_bubble_sort_ascending(array):
    start = time.time()
    bubble_sort_ascending(array)
    finish = time.time()
    elapsed = finish - start
    return f'{elapsed:.2f}'

def run_bubble_sort_descending(array):
    start = time.time()
    bubble_sort_descending(array)
    finish = time.time()
    elapsed = finish - start
    return f'{elapsed:.2f}'

def run_insertion_sort_ascending(array):
    start = time.time()
    insertion_sort_ascending(array)
    finish = time.time()
    elapsed = finish - start
    return f'{elapsed:.3f}'

def run_insertion_sort_descending(array):
    start = time.time()
    insertion_sort_ascending(array)
    finish = time.time()
    elapsed = finish - start
    return f'{elapsed:.3f}'
