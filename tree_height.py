# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    inputmethod = input()
    if "I" in inputmethod:
        nodecount = int(input())
        nodestring = input()
    elif "F" in inputmethod:
        filename = input()
        with open('test/'+filename, 'r') as read:
            nodecount = read.readline()
            nodestring = read.readline()
    array = numpy.fromstring(nodestring,sep=' ')
    array = array.astype(int)
    if -1 in array:
        root = -1
    else:
        root = array[0]
    highest_hight = 0
    hight = 1
    for i, curantelement in enumerate(array):
        temp = curantelement
        while temp != root:
            temp = array[temp]
            hight = hight + 1
        if hight > highest_hight:
            highest_hight = hight
        hight = 1
    print(highest_hight)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))