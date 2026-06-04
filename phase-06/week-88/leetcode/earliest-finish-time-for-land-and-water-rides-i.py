class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish_time = float('inf')
        
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                
                
                land_end = landStartTime[i] + landDuration[i]
                water_start = max(land_end, waterStartTime[j])
                water_end = water_start + waterDuration[j]
                
                min_finish_time = min(min_finish_time, water_end)
                
                
                water_end_first = waterStartTime[j] + waterDuration[j]
                land_start = max(water_end_first, landStartTime[i])
                land_end_second = land_start + landDuration[i]
                
                min_finish_time = min(min_finish_time, land_end_second)
                
        return min_finish_time
