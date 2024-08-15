from collections import Counter
     
def find_three(nums, dic):
    for num in nums:
        i = 1
        while i <= 10 ** 10:
            if num + i in dic and num + 2 * i in dic:
                return 3, [num, num + i, num + 2 * i]
            i *= 2
    return None
 
def find_two(nums, dic):
    for num in nums:
        i = 1
        while i <= 10 ** 10:
            if num + i in dic:
                return 2, [num, num + i]
            i *= 2
    return None
 

n = int(input().strip())
nums = sorted(map(int, input().strip().split()))
dic = Counter(nums)

# Check for sequences of 3, then 2, or return a single number
result = find_three(nums, dic) or find_two(nums, dic) or (1, [nums[0]])

length, sequence = result
print(length)
print(*sequence)
