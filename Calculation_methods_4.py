from decimal import  Decimal
from math import sin, cos, pi, e



print("i\t\t\ty_0 d_0\t\ty_i/2\t\t\t\t\t\t\td_i/2\t\t\t\t\t\t\t\t\ty_i\t\t\t\t\t\t\t\td_i")
print("-" * 170)



i = 2
while i < 132000:
    if i < 100: print(i, "\t\t\t", end='')
    else:       print(i, "\t\t",   end='')

    y = y_precise = Decimal("1")
    h = Decimal(pi) / 2 / i

    for n in range(i + 1):
        if n != 0:
            x = h * n
            y += h * y * Decimal(sin(x))
            y_precise = Decimal(e ** (1 - cos(x)))

        if n == 0:                      print(y, " ", abs(y_precise - y), "\t\t",   end='')
        elif n == i / 2 and i < 5:      print(y, " ", abs(y_precise - y), "\t\t\t", end='')
        elif n == i / 2 and i < 65000:  print(y, " ", abs(y_precise - y), "\t\t",   end='')
        elif n == i / 2 and i < 132000: print(y, " ", abs(y_precise - y), "\t",     end='')
        elif n == i:                    print(y, " ", abs(y_precise - y))

    i *= 2
