# Elliptic Curve

For an elliptic curve **_E_** over the field **_GF(p)_** given by equation

 _y<sup>2</sup> = x<sup>3</sup> + xA + B_,
 
realized:

- [ ] **Algorithm for generating a point on the curve _E_**
- [ ] **Algorithm for adding points**
- [ ] **Point doubling algorithm**
- [ ] **Algorithm for finding the integer multiple point**
- [ ] **Algorithm for finding an integer multiple point (multiplication)**
- [ ] **Algorithm for generating a divisor _D_ over a curve _E_ with a carrier _supp(D)_ of a given size _d_**
- [ ] **Miller's algorithm for calculating the value of the Weil function _f<sub> n, P</sub>_ from a divisor _D_ such that** _supp(D)_ ∩ {P, O} = ∅
- [ ] **Weil pairing**
 
 ### Modular Operations (Integer) in finite field (or Galois field) 
 
 1. _x mod n_ means “the remainder of n dividing x”. In other words, if _x = an + b_, and a, b ∈ integer as well as 0 ≤ b ≤ n − 1, then _x mod n = b_.
 2. **Inverse**: If _ax = 1 mod n_,then _a_ is the inverse of _x mod n_. There are two popular methods to solve _a_:

    • _**Method 1**_: Try every value for _a < n_ until _xa mod n = 1_.
   
    • **Method 2**: Euclidean method, which is usually used to solve the inverse of big integers, so it is recommended to use Method 1 to solve the inverse of small integers. 
