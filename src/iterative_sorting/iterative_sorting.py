import math

def foo(n):
    sq_root = int(math.sqrt(n)) # O(1) +
    for i in range(0, sq_root): # O(sqrt n)
        print(i)                  # O(1)
  
# O(1) + O(sqrt n) choose dominant term
# O(sqrt n)

print(foo(36))

def frotz(n):
    s = 0  # O(1)

    for i in range(n):  # O(n)  
        for j in range(2 * n):  # O(2 * n)
            s += i * j  # O(1)
    
    return s  # O(1)

print(frotz(36))

# 1 + (n * ((2 * n)) * 1)
# 1 + 2 * n * n * 1
# 1 + 2 * n^2
# 2 * n^2

# O(2 * n^2) <-- drop the constant
# O(n^2) <-- final runtime complexity

          




# example_list = [1, 4, 2, 7, 9, 5, 3, 6, 2, 8, 10]

# # TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc) 
#         if cur_index > smallest_index:
#             pass
#             i+=1
#         else:
#             smallest_index = cur_index
#             i+=1   
#         # TO-DO: swap
#     return arr
# print(selection_sort(example_list))


# TO-DO:  implement the Bubble Sort function below

# def bubble_sort( arr ):

#     return arr


# STRETCH: implement the Count Sort function below

# def count_sort( arr, maximum=-1 ):

#     return arr