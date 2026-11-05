arr = [-100, -5, 0, 7, 14, 22, 99]
target = 14

low = 0
high = len(arr) - 1
index = -1

while low <= high:
    mid = (low + high) // 2
    
    if arr[mid] == target:
        index = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(f"Индекс элемента {target}: {index}")
