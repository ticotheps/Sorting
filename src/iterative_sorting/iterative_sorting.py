# TO-DO: Complete the selection_sort() function below 
# O(n^2)
# Steps for Selection Sorting:
# 1) Create a variable 'min_value' to temporarily hold the currently 
#    smallest item in the list as you iterate through it (which will
#    start with the list[0] item), searching for the smallest value.
# 2) Iterate through the entire list to find the smallest item in the
#    list.
# 3) Set this item equal to a 'min_value' variable and swap this item
#    with the item that is currently in list[0]. <- this is now
#    considered the "sorted portion" of the list, while everything to
#    the right of this item is considered "unsorted".
# 4) Iterate through the list again, but ONLY beginning with the FIRST
#    index of the "unsorted portion" of the list (list[1]), setting your
#    'min_value' equal to this value as you start your second iteration.
# 5) Once you find the smallest value of the "unsorted portion" of the
#    list on the 2nd pass, swap that item with the item in the FIRST index
#    of the "unsorted portion" of the list and continue with your next
#    iteration, and so forth, until the you have no items left to iterate
#    through in the "unsorted portion" of the list.

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr
print(selection_sort([5,3,4,1,2]))


# TO-DO:  implement the Bubble Sort function below
# Bubble sort is SLOW
# O(n^2)
# Steps for Bubble Sorting:
# 1) Compare the first 2 items in a list (arr[0] and arr[1]).
# 2) Swap places only if arr[1] < arr[0].
# 3) Next, compare the next 2 items in the list (arr[1] and arr[2]).
# 4) Swap places only if arr[2] < arr[1].
# 5) Continue on to the next 2 items, and so forth, until every item
#    in the list has been iterated over once.
# 6) Restart back at the beginning of the list and follow steps 1-5.


def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5,3,4,1,2]))



# STRETCH: implement the Count Sort function below

# def count_sort( arr, maximum=-1 ):

#     return arr