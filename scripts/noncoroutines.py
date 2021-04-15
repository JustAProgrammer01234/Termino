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

if __name__ == '__main__':
    array = [5,4,2,6,8,0]
    array2 = [5,4,2,6,8,0]
    print(get_token())
    print(f"Output: {str_to_array('1 2 3 4 5')} type of output: {type(str_to_array('1 2 3 4 5'))}")
    bubble_sort_ascending(array)
    print(array)
    bubble_sort_descending(array2)
    print(array2)
