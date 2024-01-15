"""

981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"


Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

"""

class TimeMap:
    def __init__(self):
        # create a struct for TimeMap
        # { key : { timestamp : value } }
        self.timeMap = {}
        return
    
    def set(self, key, value, timestamp):
        # set key, value, timestamp 
        # case 1 : no key in timeMap
        if key not in self.timeMap.keys():
            self.timeMap[key] = {timestamp : value}
        # case 2 : key already exists
        else:
            self.timeMap[key][timestamp] = value

        return
    
    def get(self, key, timestamp):
        # if the key exists 
        if self.timeMap[key]:
            # if timestamp for the key exists 
            try:
                value = self.timeMap[key][timestamp]
            # if timestamp for key does not exists 
            except KeyError:
                timestamp_list = list(self.timeMap[key].keys())
                target = timestamp
                left = 0
                right = len(timestamp_list) - 1 
                timestamp_prev = -1 # record the position of mid 

                # update case 
                # case 1 : target greater than right pointer value 
                if target >= timestamp_list[right]:
                    print("right")
                    return self.timeMap[key][timestamp_list[right]]
                
                # case 2: target greater than left pointer value 
                if target < timestamp_list[left]:
                    print("too left")
                    return ""
                
                # case 3: target in between left and right pointer value 
                if timestamp_list[left] < target < timestamp_list[right]:
                    print("mid")
                    while left <= right:
                            mid = (left + right) // 2
                            if timestamp_list[mid] < target:
                                left = mid + 1
                                if mid > timestamp_prev:
                                    timestamp_prev = mid
                                else:
                                    continue
                            elif timestamp_list[mid] > target:
                                right = mid - 1
                                continue
                # if no timestamp prev return null
                if timestamp_prev == -1 :
                    return "null"
                else:
                    res = timestamp_list[timestamp_prev]
                    return self.timeMap[key][res]
            # if timestamp for key exists, output value 
            else:
                return value
        # if key does not exists, return null
        else:
            return "null"
        
    

if __name__ == "__main__":
    obj = TimeMap()
    obj.set('love','high',10)
    obj.set('love','low',20)
    print(obj.get('love',5))
    print(obj.get('love',10))
    print(obj.get('love',15))
    print(obj.get('love',20))
    print(obj.get('love',25))