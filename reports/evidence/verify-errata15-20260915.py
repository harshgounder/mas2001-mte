#!/usr/bin/env python3
"""Evidence for errata 15: the Chebyshev deck (S&P L10-11) Q3 slide, page 8.

The slide states:  X takes -1, -1, 3, 5 with p = 1/6, 1/6, 1/6, 1/2
and then works:    E(X) = -1/6 + 1/6 + 3/6 + 5/2 = 3
                   E(X^2) = 43/3
                   sigma^2 = 43/3 - 9 = 16/3
                   bound = 16/3

Run: python3 verify-errata15-20260915.py
Stdlib only.
"""
from fractions import Fraction as F

STATED_X   = [-1, -1, 3, 5]          # as printed on the slide
WORKED_X   = [-1,  1, 3, 5]          # what the slide's own E(X) line implies
P          = [F(1,6), F(1,6), F(1,6), F(1,2)]

def moments(xs, ps):
    n = len(xs)
    sp  = sum(ps)
    ex  = sum(x*p for x, p in zip(xs, ps))
    ex2 = sum(x*x*p for x, p in zip(xs, ps))
    return sp, ex, ex2, ex2 - ex*ex

for name, xs in (("STATED", STATED_X), ("WORKED", WORKED_X)):
    sp, ex, ex2, var = moments(xs, P)
    print(f"{name} row {xs} with p {[str(p) for p in P]}")
    print(f"   sum p      = {sp}          {'valid distribution' if sp == 1 else 'NOT a distribution'}")
    print(f"   E(X)       = {ex} = {float(ex):.4f}")
    print(f"   E(X^2)     = {ex2} = {float(ex2):.4f}")
    print(f"   Var        = {var} = {float(var):.4f}")
    print()

print("slide prints:  E(X) = 3, E(X^2) = 43/3, sigma^2 = 16/3, bound = 16/3")
print()
sp_w, ex_w, ex2_w, var_w = moments(WORKED_X, P)
sp_s, ex_s, ex2_s, var_s = moments(STATED_X, P)
print(f"E(X) as printed (3) matches the WORKED row: {ex_w == 3}")
print(f"E(X) from the STATED row is {ex_s}, not 3: {ex_s != 3}")
print(f"E(X^2) = 43/3 under both rows (squaring drops the sign): {ex2_w == ex2_s == F(43,3)}")
print(f"sigma^2 as printed (16/3) matches the WORKED row: {var_w == F(16,3)}")
print(f"sigma^2 from the STATED row would be {var_s} = {float(var_s):.4f}: {var_s != F(16,3)}")
print()

# The event is |X - 3| >= 1. Exact probability:
exact = 1 - P[2]                     # only X = 3 sits inside (2,4)
print(f"exact P(|X-3| >= 1) = 1 - P(X=3) = {exact} = {float(exact):.4f}")
print()

# Chebyshev bound 1/k^2 with k*sigma = 1, i.e. k = 1/sigma, so the bound is sigma^2.
print("bound = 1/k^2 with k*sigma = 1  =>  bound = sigma^2")
print(f"   using the WORKED sigma^2 = 16/3 = {float(F(16,3)):.4f}  -> the slide's 16/3 IS the")
print("   correct Chebyshev bound for that row")
print(f"   using the STATED sigma^2 = {var_s} = {float(var_s):.4f}  -> the bound would be {var_s}")
print()
print(f"is 16/3 above the exact probability {exact}? {F(16,3) > exact}  (so the bound holds, but")
print("it is useless: 5.33 for a probability of 0.83)")
print(f"is the bound above 1? {F(16,3) > 1}")
print()
print("CONCLUSION: the two real defects on this slide are")
print("  (1) it STATES (-1,-1,3,5) and WORKS (-1,1,3,5): E(X)=3 only holds for the latter,")
print("      and the printed sigma^2 = 16/3 inherits that, so the printed variance does not")
print("      belong to the printed distribution (which would give 65/9).")
print("  (2) the inequality is written P(|x-mu| >= k) < k^2/sigma^2; the standard form is")
print("      P(|X-mu| >= k*sigma) <= 1/k^2, so the k inside the event is not the k on the right.")
print("NOT defects (computed, not assumed): E(X^2) = 43/3 is correct either way, and the")
print("final 16/3 is the right bound for the row the working uses.")
