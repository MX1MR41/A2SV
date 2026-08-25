class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][0] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def get(self, key: str, timestamp: int) -> str:
        curr = self.dic[key]
        n = len(curr)

        ind = self.binary_search(curr, timestamp)

        if 0 <= ind < n:
            return curr[ind][1]
        elif ind == -1:
            return ""
        else:
            return curr[-1][1]
