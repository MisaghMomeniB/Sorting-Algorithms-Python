from bubble_sort import bubble_sort  # Import Bubble Sort function
from selection_sort import selection_sort  # Import Selection Sort function
from insertion_sort import insertion_sort  # Import Insertion Sort function
from quick_sort import quick_sort  # Import Quick Sort function
from merge_sort import merge_sort  # Import Merge Sort function

# Define an unsorted array
arr = [64, 25, 12, 22, 11]

# Use slicing (arr[:]) to pass a copy of the array to each function 
# to avoid modifying the original array
print("Bubble Sort:", bubble_sort(arr[:]))
print("Selection Sort:", selection_sort(arr[:]))
print("Insertion Sort:", insertion_sort(arr[:]))
print("Quick Sort:", quick_sort(arr[:]))
print("Merge Sort:", merge_sort(arr[:]))