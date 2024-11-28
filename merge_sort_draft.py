# divide and conquer 
# break down the code into smallest elements using recursion 
# based case : if len(arr) == 1
# merge sort do not use extra space, in place array sorting (require pointer k)
# 1. break down array into smallest component of 1 element in each sub array (divide)
# 2. compare the left and right sub array for ordering (conquer)
# 3. in place array sorting based on the item value comparison 


def merge_sort(input_array):
    print(f'the current dividing array {input_array}')
    
    # based check 
    # if the array has been breaked down into the smallest element 
    if len(input_array) <= 1:
        return input_array

    # define start and end pointer 
    start = 0
    end = len(input_array)
    
    # define start and end pointer
    mid = start + (end - start) // 2 
    print(f'current start pointer = {start}, mid pointer = {mid}, end pointer = {end}')

    # break down the array into smallest sections 
    Left = input_array[start:mid]
    Right = input_array[mid:end+1]

    merge_sort(Left)

    merge_sort(Right)

    # after breaking down array into smallest sub array, execute the following:

    # create three different pointers for original and its left and right 
    # need pointer k because merge sort uses array in place sorting 
    i = j = k = 0

    while i < len(Left) and j < len(Right):

        # compare size of items in left array and items in right array
        if Left[i] <= Right[j]:
            input_array[k] = Left[i]
            i += 1
        else Left[i] > Right[j]:
            input_array[k] = Right[j]
            j += 1

        k += 1

    # for edge case where the left and right array are not in same length
    while k < len(input_array):
        if i < len(Left):
            input_array[k] = Left[i]
            i += 1
        if j < len(Right):
            input_array[k] = Right[j]
            j+=1
        k += 1

    return input_array



if __name__ == "__main__":
    nums = [3,5,1,2,7,6]
    res = merge_sort(nums)
    print(res)