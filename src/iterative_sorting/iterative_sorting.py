# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    length = len(arr)
    start = 0
    smallest = 0
    current = 0
    placeholder = 0
    
    # loop through n-1 elements
    #for i in range(0, len(arr) - 1):
        #cur_index = i
        #smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    while start < length:
        smallest = arr[start]

        for i in range(start,length):
            current = arr[i]
            if current < smallest:
                smallest = current
                placeholder = i
        if arr[start] is not smallest:
            while placeholder > start:
                arr[placeholder] = arr[placeholder-1]
                arr[placeholder-1] = smallest
                placeholder -= 1
        start +=1
            
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    
    swapped = True
    first_val = 0
    sec_val = 0
    temp_val = 0
    length = len(arr)

    while swapped == True:
        
        while length > 1:
            length -=1
            complete = False


            for index in range(0, length): 
                first_val = arr[index]
                if arr[index+1] is not None:
                    sec_val = arr[index+1]
                if first_val > sec_val:
                    temp_val = first_val
                    first_val = sec_val
                    sec_val = temp_val
                    temp_val = 0
                    arr[index] = first_val
                    if arr[index+1] is not None:
                        arr[index+1] = sec_val
                    swapped = True
                
                else:
                    swapped = False
        
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
