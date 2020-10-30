from sympy import sympify, simplify
from sympy import Symbol, Derivative, Integral, Rational
a=sympify("2*x+3*x+3*y+2**3")
print(a)
b=sympify("(x+1)/(x*x-1)")
print(b)
c=simplify(b)
print(c)

