# Elliptic Curve

For an elliptic curve **_E_** over the field **_GF(p)_** given by short Weierstrass equation

 _y<sup>2</sup> = x<sup>3</sup> + Ax + B_,
 
realized:

- [ ] **Algorithm for generating a point on the curve _E_**
- [ ] **Algorithm for adding points**
- [ ] **Point doubling algorithm**
- [ ] **Algorithm for finding the integer multiple point**
- [ ] **Algorithm for finding an integer multiple point (Scalar multiplication)**
- [ ] **Algorithm for generating a divisor _D_ over a curve _E_ with a carrier _supp(D)_ of a given size _d_**
- [ ] **Miller's algorithm for calculating the value of the Weil function _f<sub> n, P</sub>_ from a divisor _D_ such that** _supp(D)_ ∩ {P, O} = ∅
- [ ] **Weil pairing**
 
 ### Modular Operations (Integer) in finite field (or Galois field) 
 
 1. _x mod n_ means “the remainder of n dividing x”. In other words, if _x = an + b_, and a, b ∈ integer as well as 0 ≤ b ≤ n − 1, then _x mod n = b_.
 2. **Inverse**: If _ax = 1 mod n_,then _a_ is the inverse of _x mod n_. There are two popular methods to solve _a_:

    • _**Method 1**_: Try every value for _a < n_ until _xa mod n = 1_.
   
    • _**Method 2**_: Euclidean method, which is usually used to solve the inverse of big integers, so it is recommended to use Method 1 to solve the inverse of small integers. 

### Elliptic Curve Points Operation

A point _P(x<sub>0</sub>, y<sub>0</sub>)_ on elliptic curve _E_ means: its coordinates _x<sub>0</sub>_ and _y<sub>0</sub>_ are elements in the field, and the coordinates _x<sub>0</sub>_ and _y<sub>0</sub>_ satisfy Equation.

1. **Elliptic curve points addition**:
Let _P, Q_ and _R_ be three points on an elliptic curve. Points addition P + Q = R.
2. **Elliptic curve points doubling**:
Let _P, Q_ be two points on an elliptic curve. Points doubling P + P = 2P = Q
3. **Scalar multiplication**: Let _P_ be a point on curve _E_ defined in equation
   - Scalar multiplication _nP_ is defined as _nP = P + P + P + ... + P_ (_n_ times), where _n_ is an integer; _nP_ is also a point on the same curve _E_.
   - The minimal positive integer a for _aP = O_ is called the **order of _P_** .
   - Scalar multiplication is extensively required in elliptic curve cryptosystems.
   
### Divisor 

A divisor _D_ on curve _E_ is a convenient way to denote a **multi-set of points on _E_**, written as the formal sum 
![Divisor formula](https://github.com/ElizaLo/Cryptography/blob/master/Elliptic%20Curve/img/Divisor.png)
- The set of all divisors on _E_ is denoted by _Div<sub>F<sub>q</sub></sub>(E)_ and forms a group, where addition of divisors is natural.
- The zero divisor: it is the divisor with all n<sub>P</sub> = 0, the zero divisor _0 ∈ Div<sub>F<sub>q</sub></sub>(E)_.
- If the field _F<sub>q</sub>_ is not specific, it can be omitted and simply written as _Div(E)_
to denote the group of divisors.

### The Divisor of a Function _f_ on _E_

The divisor of a function _f_ on _E_ is used to denote the intersection points (and their multiplicities) of _f_ and _E_.

### The Weil pairing


The Weil pairing, which is denoted by _e<sub>m</sub>_, takes as input a pair of points _P, Q ∈ E[m]_ and gives as output an _m<sup>th</sup> root of unity _e<sub>m</sub>(P, Q)_. The bilinearity of the Weil pairing is expressed by the equations

_e<sub>m</sub>(P<sub>1</sub> + P<sub>2</sub>, Q) = e<sub>m</sub>(P<sub>1</sub>, Q) * e<sub>m</sub>(P<sub></sub>2, Q),_

_e<sub>m</sub>(P, Q<sub>1</sub> + Q<sub>2</sub>) = e<sub>m</sub>(P, Q<sub>1</sub>) * e<sub>m</sub>(P, Q<sub>2</sub>)._

The **Weil pairing** of _P_ and _Q_ is the quantity

![Weil](https://github.com/ElizaLo/Cryptography/blob/master/Elliptic%20Curve/img/Weil%20formula.png)

where _S ∈ E_ is any point satisfying _S ∉ {O, P, −Q, P − Q}_. (This ensures that all of the quantities on the right-hand side of are defined and nonzero.) One can check that the value of _e<sub>m</sub>(P,Q)_ does not depend on the choice of _f<sub>P</sub>_, _f<sub>Q</sub>_, and _S_.
