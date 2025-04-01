def hasDuplicate(nums):
    new_set = set()
    for i in nums:
        if i in new_set:
            return True
        new_set.add(i)
    return False

print(hasDuplicate([1,2,3,3]))
print(hasDuplicate([1,2,3,4]))
