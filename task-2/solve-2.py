count = int(input())
total_sum = 0

for _ in range(count):
    num = int(input())
    if num % 6 == 0 and num % 10 == 4:
        total_sum += num

print(total_sum)
