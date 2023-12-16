class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        range_map = defaultdict(list)
        visited = defaultdict(bool)
        max_length = 0
        
        for num in nums:
            if visited[num]:
                continue 
            
            visited[num] = True
            left, right = num, num
            
            if range_map[num + 1]:
                right = range_map[num + 1][0]
                
            if range_map[num - 1]:
                left = range_map[num - 1][1]
                
            range_map[right] = [right, left]
            range_map[left] = [right, left]
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
