# Examples from Beej's Lecture
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

# ---------------------------------------------

# O(8 * n) === O(n) <-- both of these simplify to O(n) runtime because we're more interested in the shape of the curve
# O(2 * n) === O(n)

# O(4 * n!) === O(n!) <-- both of these simplify to O(n!) runtime
# O(2 * n!) === O(n!)
# O(n^2)

# ---------------------------------------------

# def bar(x):
#     sum = 0
#     for i in range(0, 1463):
#         i += sum
#         for j in range(0, x):
#             for k in range(x, x + 15):
#                 sum += 1

# ---------------------------------------------

# def search(list, value):
#     for i in list:
#         if i == value:
#             return True
#     return False

# # O(n)

# print(search([1,2,3,4,5,6,7,8,9,10], 7))

# ---------------------------------------------

# def bad_binary_search(l, v):
#     sort(l)           # O(n log n)
#     bsearch(l, v)     # O(log n)

# O(n log n) + O(log n)
# O(n log n)

# ---------------------------------------------

class Book:
    def __init__(self, t, a, g):
        self.title: t
        self.author: a
        self.genre: g

def insertion_sort(books):
    for i in range(1, len(books)):
        temp = books[i]
        j = i

        while j > 0 and temp.genre < books[j - 1].genre:
            books[j] = books[j-1]  # scoot books over to make room
            j -= 1
            
    #  j is now the index of where we want to place the book
    return books
        