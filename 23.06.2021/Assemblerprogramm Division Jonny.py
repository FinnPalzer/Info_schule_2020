def division(dividend, divisor):
    ergebnis = 0

    while dividend > 0:
        dividend = dividend - divisor
        ergebnis = ergebnis +1
    return ergebnis
