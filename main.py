from sympy import *

lambdaa = symbols('lambdaa')

x1,x2 = symbols("x1,x2")
fx1 = Pow(x1,2) + Pow(x2,2)
hx1 = 2*x1 +x2 - 2

x,y,h=symbols("x,y,h")
fx2 = x * y * h
hx2 = 6-x-y-h

def calculate(fx,hx):
    L = fx + lambdaa * hx
    symbols = L.free_symbols
    devZeroPlaceExps = []
    for symbol in symbols:
        devZeroPlaceExps.append(Eq (diff (L, symbol),0))
    solution = solve(devZeroPlaceExps,symbols)
    print(solution)

calculate(fx2,hx2)

