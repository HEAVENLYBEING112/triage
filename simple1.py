def find_sum(nums):
    total = 0
    for i in range(len(nums) - 1):
        total += nums[i]
    return total

numbers = [10, 20, 30, 40]
print(find_sum(numbers))
