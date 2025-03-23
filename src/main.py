# Import sorting functions from respective files
from bubble_sort import bubble_sort  
from selection_sort import selection_sort  
from insertion_sort import insertion_sort  
from quick_sort import quick_sort  
from merge_sort import merge_sort  

# Define an unsorted array
arr = [64, 25, 12, 22, 11]

# Dictionary to store sorting functions
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}

# Print the original unsorted array
print("Original Array:", arr)

# Loop through sorting algorithms and print sorted arrays
for name, sort_function in sorting_algorithms.items():
    print(f"{name}: {sort_function(arr[:])}")  # Passing a copy to avoid modifying the original array