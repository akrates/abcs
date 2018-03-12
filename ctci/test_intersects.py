# ctci 16.3

from intersects import *

segment1 = ((1,1), (4,4))
segment2 = ((1,1), (3,1))
segment3 = ((0,2), (3,2))
segment4 = ((2,2), (5,2))
segment5 = ((6,2), (8,2))

# same line, no overlap
def test_same_line():
    intersects(segment4, segment5)

# intersection at endpoint
def test_at_endpoint():
    intersects(segment1, segment2)

# intersection proper
def test_intersection_proper():
    intersects(segment1, segment3)

# overlap in same infinite line
def test_overlap():
    intersects(segment3, segment4)

# endpoint in x and y range but no overlap
def test_collinear_no_overlap():
    intersects(segment1, segment4)


