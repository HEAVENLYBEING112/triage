def find_max(numbers):
    max = numbers[0]
    
    for i in range(len(numbers)):
        if numbers[i] > max:
            max == numbers[i]
    
    return max

nums = []
result = find_max(nums)

print("Max value is:", result)
