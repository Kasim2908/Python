def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: # Check if the current element matches the target
            return i  # Return the index if found
    return -1  # Return -1 if the target is not found
arr = [10, 20, 30, 40, 50]
target = 50
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
