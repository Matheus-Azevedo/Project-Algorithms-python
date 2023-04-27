def find_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        try:
            nums[i] = int(nums[i])
        except ValueError:
            return False
        else:
            if nums[i] < 1:
                return False
            if nums[i] == nums[i-1]:
                return nums[i]

    return False
