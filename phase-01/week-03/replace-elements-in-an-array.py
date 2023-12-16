class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {value: index for index, value in enumerate(nums)}

        for operation in operations:
            value_to_replace, new_value = operation
            index_to_replace = index_map[value_to_replace]

            nums[index_to_replace] = new_value
            del index_map[value_to_replace]
            index_map[new_value] = index_to_replace

        return nums
