numbers = [10, 20, 30, 40, 50]

total = 0
for i in range(len(numbers)):
    total += numbers[i]

average = total / len(numbers)
if average is None or len(numbers) == 0:
    print('Error: Cannot calculate average on empty list')
else:
    print('Average is:', average)

print('Program completed')