def kapital(t):
    if (t==0):
        return 1000
    else:
        return kapital(t-1) + kapital(t-1)*0.05
