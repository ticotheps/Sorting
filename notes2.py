# What is recursion?
# A process in which a function calls itself as a subroutine.

# What is 'space complexity'?
# The amount of memory that an algorithm uses up.

#----------------------------------------------------------

# Example 1
# Space Complexity: O(1)

# for i in range(a, b):
#     print(i)

#----------------------------------------------------------

# Example 2 (pseudocode)
# Space Complexity: 
# Runtime Complexity: O(n)
# printing a list from a to b:
    # print a
    # print list from a+1 to b

# def loop(a, b):  # O(n) === O(b-a)
#     if a == b:
#         return

#     print(a)

#     loop(a+1, b)  # b = base case

# loop(0,10)

#----------------------------------------------------------

# Example 3
# Space Complexity: 
# Runtime Complexity:
# sum(a, b) === a + sum(a+1, b)

# Stack Frames
#------- call #0
# a == 0
# b == 1
#------- call #1
# a == 1
# b == 1
#-------

# def sum(a, b):  # O(n) === O(b-a)
#     if a == b:  # Base Cases are always in the form of a conditional
#         return 0

#     return a + sum(a+1, b)

# x = sum(0, 4)
# #  runs "0 + 1 + 2 + 3 + 0"

# print(x)

#----------------------------------------------------------

# Example 4
# Space Complexity: 
# Runtime Complexity: O(2^n)
counter = 0

def foo(n):
    global counter

    if n <= 0:
        return
    
    # print(n)
    counter += 1

    # Each call makes two calls, so O(2^n)
    # If each call makes 3 calls, then O(3^n)
    foo(n-1)
    foo(n-2)

# foo(1)    # 1
# foo(2)    # 2
# foo(3)    # 4
foo(4)    # 7
# foo(5)    # 12
# foo(6)      # 20

# O(2^n)

print(counter)

#----------------------------------------------------------