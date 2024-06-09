def message_delivery_system(n,k,timestamps_list, messages_list):
    buffer_dict = {}
    delivered_list = []
    for i in range (0,n):
        cur_time = int(timestamps_list[i])
        cur_msg = messages_list[i]
        
        if cur_msg not in buffer_dict.keys():
            buffer_dict[cur_msg] = cur_time + k
            delivered_list.append('true')
        else:
            expire_time = buffer_dict[cur_msg]
            if cur_time <= expire_time:
                delivered_list.append('false')
            else:
                buffer_dict[cur_msg] = cur_time + k 
                delivered_list.append('true')
    
    return delivered_list

if __name__ == "__main__":
    n = 6
    k = 5
    timestamps = [1,4,5,10,11,14]
    messages = ["hello","bye","bye","hello","bye","hello"]
    res_list = message_delivery_system(6,5,timestamps,messages)
    print(res_list)