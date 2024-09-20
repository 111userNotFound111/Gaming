"""
Declare 2-d array arr of n empty arrays, ALl arrays are zero indexed
Declare an integer LastAns and initialize it to 0
Declare an AnsArray to store answers 
There are two types of queries, given as an array of strings 
Type 1: 1 x y
idx = ((x XOR lastAns) % n)
append y to arr[idx]

Type 2: 2 x y 
idx = ((x XOR lastAns) % n)
assign arr[idx][y % size(arr[idx])] to lastAns
store the new value of lastAns to answers array

return AnsArray which contains changes to LastAns

"""
# type one query 
def type_one(input_array_2d, last_answer, n, x, y):
    index = (x ^ last_answer) % n
    input_array_2d[index].append(y)
    return input_array_2d

# type two query 
# update last_answer and added to the input_answer_list
def type_two(input_array_2d, input_answ_list, last_answer, n, x, y):
    index = (x ^ last_answer) % n
    last_answer = input_array_2d[index][ y % len(input_array_2d[index])]
    input_answ_list.append(last_answer)
    return last_answer, input_answ_list


def dynamicArray(n, queries):
    # the ans_list array is required by the question 
    ans_list = []
    array_2d = [ [] for i in range(n) ] # creating list of array with given value 
    lastAns = 0
    # queries is a list of lists that contains query in the form of array
    for query in queries:
        # first value of each query indicates the query type
        if int(query[0]) == 1:
            x = query[1]
            y = query[2]
            array_2d = type_one(array_2d, lastAns, n, x, y)
        if int(query[0]) == 2:
            x = query[1]
            y = query[2]
            lastAns_new, ans_list = type_two(array_2d, ans_list, lastAns, n ,x,y)
            if lastAns != lastAns_new:
                lastAns = lastAns_new
                print(lastAns)
    return ans_list


if __name__ == "__main__":
    solution = dynamicArray(2,[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])
    print(solution)
