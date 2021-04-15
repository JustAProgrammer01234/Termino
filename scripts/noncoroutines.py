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

if __name__ == '__main__':
    array = [5,4,2,6,8,0]
    array2 = [5,4,2,6,8,0]
    array3 = [5,3,5,6,8,9,6,3,1]
    array4 = [6,54,6,7,8,6,4,3,4,5,67,8]

    array_clone = array[:]
    array_clone.sort()

    array2_clone = array2[:]
    array2_clone.sort()
    array2_clone.reverse()

    array3_clone = array3[:]
    array3_clone.sort()

    array4_clone = array4[:]
    array4_clone.sort()
    array4_clone.reverse()

    print(get_token())
    print(f"Output: {str_to_array('1 2 3 4 5')} type of output: {type(str_to_array('1 2 3 4 5'))}")

    bubble_sort_ascending(array)
    print(array)
    assert array == array_clone

    bubble_sort_descending(array2)
    print(array2)
    assert array2 == array2_clone

    insertion_sort_ascending(array3)
    print(array3)
    assert array3 == array3_clone

    insertion_sort_descending(array4)
    print(array4)
    assert array4 == array4_clone
