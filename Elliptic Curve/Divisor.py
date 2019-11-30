from EllipticCurve import *
from EuclideanAlg import *
import copy


def Miller(P, Q, r):
    """
    Calculate function by Miller's Algorithm
    :param P: A point over E which has order r
    :param Q: A point over E which has order r to apply function f_P
    :param r: The order of P, Q on E
    :return: f_P(Q)
    """
    assert(P.A == Q.A and P.B == Q.B)
    assert ((not P.inf) and (not Q.inf))
    def g(P, Q, R):
        # if \lambda is infinity
        if (P == Q and P.y == 0) or (P != Q and P.x == Q.x):
          return R.x - P.x
        L = P.line_coeff(Q)
        p = R.y - P.y - L * (R.x - P.x)
        q = R.x + P.x + Q.x - L * L
        return p * moduloInverse(q, P.mod)
    R = copy.deepcopy(P)
    f = 1
    rRev = 0
    n = 0
    while r > 0:
        rRev <<= 1
        rRev += r % 2
        r >>= 1
        n += 1
    rRev >>= 1
    for i in range(n-1):
        R *= 2
        f = f * f * g(R, R, Q)
        if rRev % 2 == 1:
            R += P
            f = f * g(R, P, Q)
        rRev >>= 1
    return f % P.mod

def Weil(P, Q, r, S):
    """
    Calculate Weil Pairing
    :param P: A point over E which has order r
    :param Q: A point over E which has order r
    :param r: The order of P, Q on E
    :param S: [Optional] A random point on E
    :return: e_r(P, Q)
    """
    assert(onSameCurve(P, Q, S))
    num = Miller(P, Q + S, r) * Miller(Q, -S, r)
    denom = Miller(P, S, r) * Miller(Q, P - S, r)
    return num * moduloInverse(denom, P.mod) % P.mod



'''
def Miller(P, Q, r):
    """

    :param P:
    :param Q:
    :param r:
    :return:
    """
    assert(P.A == Q.A and P.B == Q.B)
    assert ((not P.inf) and (not Q.inf))
    R = copy.deepcopy(P)
    f = 1
    rRev = 0
    n = 0
    Q2 = 2 * Q
    while r > 0:
        rRev <<= 1
        rRev += r % 2
        r >>= 1
        n += 1
    rRev >>= 1
    for i in range(n-1):
        lQ = l(R, R, Q)
        lQ2 = l(R, R, Q2)
        R *= 2
        vQ = v(R, Q)
        vQ2 = v(R, Q2)
        f = f * f * lQ2 * vQ * moduloInverse(lQ * vQ2, P.mod) % P.mod
        if rRev % 2 == 1:
            lQ = l(R, P, Q)
            lQ2 = l(R, P, Q2)
            R += P
            vQ = v(R, Q)
            vQ2 = v(R, Q2)
            f = f * lQ2* vQ * moduloInverse(lQ * vQ2, P.mod)
        rRev >>= 1
    return f
'''
