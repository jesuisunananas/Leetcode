def twoSum(numbers, target):
    front = 0
    back = len(numbers) - 1
    while front < back:
        if numbers[front] + numbers[back] > target:
            back -= 1
        elif numbers[front] + numbers[back] < target:
            front += 1
        else:
            return [front + 1, back + 1]

print(twoSum([1,2,3,4], 3))