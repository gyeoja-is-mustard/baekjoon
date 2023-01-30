import sys

aim = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))

min_count = abs(100-aim)

for nums in range(1000001):
    nums = str(nums)
    
    for i in range(len(nums)):
        if int(nums[i]) in broken:
            break
        
        elif i == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - aim) + len(nums))
            
print(min_count)
            