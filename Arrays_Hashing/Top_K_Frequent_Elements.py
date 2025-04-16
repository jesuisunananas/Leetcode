def topKFrequent(nums, k):
    frequency_map = {}
    for i in nums:
        if i not in frequency_map:
            frequency_map[i] = 0
        frequency_map[i] += 1
    arr = []
    for a, num in frequency_map.items():
        arr.append([num, a])
    arr.sort()
    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res

print(topKFrequent([1,2,2,3,3,3], 2)) # [3,2]
print(topKFrequent([7,7], 1)) # [7]