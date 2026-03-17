def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val

nums = []
result = find_max(nums)

print("Max value is:", result if result else 'None')