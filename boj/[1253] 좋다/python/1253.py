import sys

N = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]
numbers.sort()
count = 0

for i, number in enumerate(numbers):
    temp = numbers[:i] + numbers[i + 1:]
    start, end = 0, len(temp) - 1
    while start < end:
        if temp[start] + temp[end] < number:
            start += 1
        elif temp[start] + temp[end] > number:
            end -= 1
        else:
            count += 1
            break
print(count)
