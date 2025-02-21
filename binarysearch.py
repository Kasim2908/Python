def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle element
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Return the index of the target
        
        # If target is smaller, it can only be in the left half
        elif arr[mid] > target:
            high = mid - 1
        
        # If target is larger, it can only be in the right half
        else:
            low = mid + 1
    
    return -1  # Target not found
# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
