# TO-DO: complete the helper function below to merge 2 sorted arrays

arrA = [3, 12, 16, 8, 4 , 19, 9, 1, 13]
arrB = [15, 7, 14, 17, 18, 11 , 2, 5, 10, 6]

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # Create 'checked_item_1' variable to hold value of first item being compared.

    # Create 'checked_item_2' variable to hold value of second item being compared.

    # Create new 'arrC' array to hold values of sorted items during comparisons.

    # Set 'checked_item_1' to arrA[0].

    # Set 'checked_item_2' to arrB[0].

    # Compare 'checked_item_1' and 'checked_item_2' and append the smaller of the 
    # two items into the merged_arr.

    # Continue comparing items until one array has been eliminated.

    # Merge the remaining array into the merged_arr.

    
    return merged_arr

print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below USING RECURSION

# def merge_sort( arr ):
#     # TO-DO

#     return arr


# STRETCH: implement an in-place merge sort algorithm

# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
