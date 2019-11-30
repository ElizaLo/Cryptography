from EuclideanAlg import *

class EPoint:

    def __init__(self, A, B, x, y, mod, inf = False):
        assert(0 <= A <= mod and 0 <= B <= mod)
        self.A = A
        self.B = B
        self.x = x % mod
        self.y = y % mod
        self.mod = mod
        self.inf = inf
        assert((self.y ** 2) % mod == (self.x ** 3 + A * x + B) % mod)

    def line_coeff(self, other):
        """
        Лямбда
        """
        if self.x != other.x or self.y != other.y:
            if self.x == other.x:
                return EPoint(self.A, self.B, self.x, self.y, self.mod, True)
            l = (other.y - self.y) * moduloInverse(other.x - self.x, self.mod) % self.mod # l - lambda
        else:
            if self.y == 0:
                return EPoint(self.A, self.B, self.x, self.y, self.mod, True)
            l = (3 * self.x ** 2 + self.A) * moduloInverse(2 * self.y, self.mod) % self.mod
        return l

    def __add__(self, other):
        assert (onSameCurve(self ,other)) # если точки не лежат на одной и той же кривой
        if self.inf:
            return self
        if other.inf:
            return other
        l = self.line_coeff(other)
        if isinstance(l, EPoint):
            return l
        x = (l ** 2 - self.x - other.x) % self.mod
        y = (l * (self.x - x) - self.y) % self.mod
        return EPoint(self.A, self.B, x, y, self.mod)

    def __iadd__(self, other):
        return self + other

    def __neg__(self):
        return EPoint(self.A, self.B, self.x, -self.y, self.mod, self.inf)

    def __eq__(self, other):
        return onSameCurve(self, other) \
               and ((self.x == other.x and self.y == other.y) or (self.inf == True and other.inf == True))

    def __ne__(self, other):
        return not self == other

    def __rmul__(self, other): # self - точка на кривой, other - натуральное число
        assert(other != 0)
        negate = False
        if other < 0:
            negate = True
            other = - other
        init = False
        powerOf2 = self
        while True:
            if other % 2 == 1:
                if init:
                    res += powerOf2
                else:
                    res = powerOf2
                    init = True
            other >>= 1 # побитовый сдвиг вправо на один бит, то же самое что целочисленно / 2
            if other == 0:
                break
            powerOf2 += powerOf2
        if negate:
            res = - res
        return res

    def __imul__(self, other):
        return other * self


def onSameCurve(*points):
    for P, Q in zip(points[:-1], points[1:]):
       if P.A != Q.A or P.B != Q.B or P.mod != Q.mod:
           return False
    return True
'''
def l(P, Q, R):
    """
    функция, задающая прямую линию, проходящую через точки P и Q
    :param P:
    :param Q:
    :param R:
    :return:
    """
    assert (onSameCurve(P, Q, R))
    if P == Q:
        assert (P.y != 0)
        res = R.y
        denom  = moduloInverse(2 * P.y, P.mod)
        res -= R.x * (3 * P.x ** 2 + P.A) * denom
        res -= (- P.y + 2 * P.A * P.x + 3 * P.B) * denom
        res %= P.mod
    else:
        assert (P.x != Q.x)
        res = R.y
        denom = moduloInverse(Q.x - P.x, P.mod)
        res -= R.x * (Q.y - P.y) * denom
        res -= (Q.x * P.y - P.x * Q.y) * denom
        res %= P.mod
    return res

def v(P, R):
    """
    функция, задающая вертикальную линию, проходящую через точку P
    :param P:
    :param R:
    :return:
    """
    assert (onSameCurve(P, R))
    return (R.x - P.x) % P.mod
'''
