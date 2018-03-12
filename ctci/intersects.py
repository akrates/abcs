#!/usr/bin/env python

# ctci 16.3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def ccw(A, B, C):
    """
    Determine orientation of three points; return True if counterclockwise
    Assume A is left-most point though it doesn't have to be for the equation to work
    """
    if (B.y - A.y) * (C.x - A.x) < (B.x - A.x) * (C.x - A.x):
        return True

def slope(A, B):
    if A.y == B.y:
        return 0 # horizontal line
    if A.x == B.x:
        return None # vertical
    return (B.y - A.y)/(B.x - A.x)


def intercept(A, B):
    return A.y - slope(A, B) * A.x


def intersects(s1, s2):
    """
    Return True if two line segments intersect
    """
    A = Point(s1[0][0], s1[0][1])
    B = Point(s1[1][0], s1[1][1])
    C = Point(s2[0][0], s2[0][1])
    D = Point(s2[1][0], s2[1][1])

    if A == C or B == C:
        return C
    if A == D or B == D:
        return D

    if ccw(A, B, C) != ccw(B, C, D): # segments overlap
        # compute intersection
        slope1 = slope(A, B)
        slope2 = slope(C, D)

        if slope1 == slope2:
            return float('Inf') # parallel and overlapping

        intercept1 = intercept(A, B)
        intercept2 = intercept(C, D)
        x = (intercept2 - intercept1)/(slope1 - slope2)
        y = slope1 * x + intercept1
        return (x, y)


"""
Notes:

classes need init, repr, and perhaps eq
float('Inf')
TODO: Figure out a better way to extract line segment coordinates
TODO: Check all edge cases, including non-integer intersection point
TODO: Add diagrams for problem statement and test cases

"""
