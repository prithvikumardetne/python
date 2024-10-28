def mode(nums: list):
    d = {}
    for i in nums:
        d[i] = nums.count(i)
    return [k for k, v in d.items() if v == max(d.values())]

nums = [1,2,3]
mode(nums)