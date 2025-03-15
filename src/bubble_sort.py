def bubble_sort(arr):
    n = len(arr)  # Get the length of the array

    # Outer loop to control the number of passes
    for i in range(n):
        
        # Inner loop for comparing and swapping elements
        # With each pass, the largest element moves to the correct position
        for j in range(0, n - i - 1):
            
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr  # Return the sorted array