size = int(input())
result = [0] * size
numbers = list(map(int, input().split()))
size = 0
for i in numbers:
    start = -1
    end = size
    while end - start != 1:
        mid = (end + start) // 2
        if numbers[mid] < i:
            start = mid
        else:
            end = mid
    if end == size:
        size += 1
    numbers[end] = i
print(size)
