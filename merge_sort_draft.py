# divide and conquer 
# part 1: Mapping all elements in array 
# part 2: reduce all mapped elements (sort and arrange)
def merge_sort(input_array):
    print(f'the current dividing array {input_array}')
    # part 1: sort the numbers 
    if len(input_array) > 1:
        mid = len(input_array) // 2
        # divide into two parts
        L = input_array[:mid]
        R = input_array[mid:]
        # this divides array into single number
        merge_sort(L)
        merge_sort(R)


        # part 2 : after mapping the element, start sorting on input array
        # i : pointer for L array   j:pointer for R array   k: pointer for sorted_array
        i = j = k = 0
        # sort L and R and store output in sorted_array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                input_array[k] = L[i]
                i += 1
            else:
                input_array[k] = R[j]
                j += 1
            k += 1
        # check if there are left elements 
        while i < len(L):
            input_array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            input_array[k] = R[j]
            j += 1
            k += 1
    
    print(input_array)



if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(nums)