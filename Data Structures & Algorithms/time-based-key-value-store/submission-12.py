class TimeMap:
    # ["TimeMap", 
    # "set", ["foo", "bar", 1], 
    # "get", ["foo", 1], 
    # "get", ["foo", 3],
    # "set", ["foo", "bar2", 4], 
    # "get", ["foo", 4], 
    # "get", ["foo", 5]]
    def __init__(self):
        # (key, timestamp) -> value 
        self.mappings = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mappings[key].append([value, timestamp])  

    # foo -> [([bar, 1], [bar2, 3)]
    def get(self, key: str, timestamp: int) -> str:
        if not key: return ""
        values = self.mappings[key]
        left = 0
        right = len(values) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res




        
