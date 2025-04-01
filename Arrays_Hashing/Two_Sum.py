def twoSum(nums, target):
    emptyDict = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in emptyDict:
            return [emptyDict[diff], i]
        emptyDict[n] = i
    
print(twoSum([3,4,5,6], 7))
print(twoSum([4,5,6], 10))
print(twoSum([5,5], 10))