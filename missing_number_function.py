

nums = [3,7,1,2,8,4,5]
def find_missing(nums):
    # Calculate sum of all elements in the input list
    sum_of_elements = sum(nums)
    
    # There is exactly one number missing 
    n = len(nums) + 1
    actual_sum = int((n * ( n + 1 ) ) / 2)
    return actual_sum - sum_of_elements