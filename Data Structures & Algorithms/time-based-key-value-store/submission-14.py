class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key)

        if not vals:
            return ""
        
        left = 0
        right = len(vals) - 1
        res = ""
        print(key, timestamp, vals)
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if vals[mid][1] == timestamp:
                res = vals[mid][0]
                break
            elif vals[mid][1] > timestamp:
                right = mid - 1
            else:
                res = vals[mid][0]
                left = mid + 1
        
        return res

        
