def find_duplicate(nums):
    if not nums or isinstance(nums, str) or len(nums) <= 1:
        return False
    seen = set()
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        if num in seen:
            return num
        seen.add(num)
    return False
