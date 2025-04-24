def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if k > len(nums):
        k = k % len(nums)
    def reverse(first, last):
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)