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

# Example 3 (pseudocode)
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

def sum(a, b):  # O(n) === O(b-a)
    if a == b:  # Base Cases are always in the form of a conditional
        return 0

    return a + sum(a+1, b)

x = sum(0, 4)
#  runs "0 + 1 + 2 + 3 + 0"

print(x)