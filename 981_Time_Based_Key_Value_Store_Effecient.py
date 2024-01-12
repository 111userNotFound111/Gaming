class TimeMap:

    def __init__(self):
        # the stored struct : {key : [ [value, timestamp] ] }
        self.timemap_store = {}

    def set(self, key, value, timestamp):
        # set key, value, timestamp 
        # if key does not exist, initialize a list
        if key not in self.timemap_store.keys():
            self.timemap_store[key] = []
        # add new value, timestamp to key
        self.timemap_store[key].append([value, timestamp])

    def get(self, key, timestamp):
        res = ""
        values_list = self.timemap_store.get(key,[])
        left = 0  
        right = len(values_list) - 1 

        while left <= right:

            mid = (left + right) // 2
            
            if values_list[mid][1] <= timestamp:
                res= values_list[mid][0]
                left = mid + 1

            else:
                right = mid - 1
            
        return res

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    obj.set("foo", "bar2", 4)
    print(obj.get("foo",3))