"""
    insert an array and sort the array in place 
    
    input: [3,1,4,2,5]
    output: [1,2,3,4,5]
    
    and sort the new inserted element in place 
    input: [3,1,4,2,5], 6
    output: [1,2,3,4,5,6]
    
"""


# # in place insertion sorting 
# # insertion sort uses two pointer method to loop and sort array
# # insertion sort the array in place 
# def insert_sort(input_arr, low, high ):
#     # two pointer method 
#     # define a pointer (i) at beginning and a pointer (j) after the first pointer 
#     for i in range (1,len(input_arr)):
#         j = i - 1
#         # for each pointer i, check if all the number in front are in ascending order
#         while j >= 0 and input_arr[j] > input_arr[j+1]:
#                 temp = input_arr[j]
#                 input_arr[j] = input_arr[j+1]
#                 input_arr[j+1] = temp
#                 j -= 1
    
#     return input_arr


# insertion using recursions and pointers
# two recursive sections:
#   1. break down the entire array to smallest sub array from large to small 
#   2. for the sub-array, sort the elements 
def insert_sort(arr, end=None):
    # part 1: break down the large array into small subarray

    # end is the end pointer of the array
    if end == None:
        end = len(arr)
    
    # base case 
    if end <= 1:
        return
    
    # recursive case
    insert_sort(arr, end-1)

    # sort the elements 
    fast = end
    slow = end - 1

    recursive_sort(arr, fast, slow)

# part 2: sort the elements within the sub array
# move the current value to the front if it's smaller 
def recursive_sort(arr, fast_pointer, slow_pointer):

    # base case 
    if slow_pointer < 0 or fast_pointer>=len(arr):
        return
    
    print(arr, fast_pointer, slow_pointer)
    if arr[slow_pointer] > arr[fast_pointer]:
        temp = arr[slow_pointer]
        arr[slow_pointer] = arr[fast_pointer]
        arr[fast_pointer] = temp
    
    fast_pointer = slow_pointer
    slow_pointer -= 1
    
    recursive_sort(arr, fast_pointer, slow_pointer)
    
    return arr


# function execution
if __name__ == "__main__":
    input_array = [3,1,4,2,5]
    res = insert_sort(input_array)
    print(res)