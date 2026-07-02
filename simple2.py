def count_even(nums):
    count = 0
    for num in nums:
        if num % 2 == 1:
            count += 1
    return count

print(count_even([2, 3, 4, 5, 6]))
