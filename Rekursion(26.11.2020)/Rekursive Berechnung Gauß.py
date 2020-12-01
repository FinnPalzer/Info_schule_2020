def gauss(n):
    if n == 0:
        return 0
    else: 
        return gauss(n-1) + n