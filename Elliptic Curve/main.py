from EuclideanAlg import *
from EllipticCurve import *
from Divisor import *

P = EPoint(3, 0, 2, 2, 5)
Q = EPoint(3, 0, 1, 2, 5)
# R = Q + P

# print(R.x, R.y)

# R = 3 * Q
#print(R.x, R.y)

#R = Q

#for k in range(5):
#    R += Q
#    print(R.inf)

f = Miller(Q, P, 5)
print(f)
