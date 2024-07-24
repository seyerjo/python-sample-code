#  MAIN CODE

import sys

"""
The default limit is 1000 recursive calls. It can be seen by calling
'sys.getrecursionlimit()'. The maximum size of the recursion stack can be
changed using the 'sys.setrecursionlimit(n)' statement. However, if this
limit is being reached, it is usually a good idea to think about whether
the recursive algorithm is really the one that best solves the problem.

"""
print(sys.getrecursionlimit())
print("\n")

sys.setrecursionlimit(999)
print(sys.getrecursionlimit())
print("\n")

sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())
print("\n")
