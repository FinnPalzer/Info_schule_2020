def hanoi(n, stab1, stab2, stab3):
    if(n==1):
        print(n,". Scheibe von",stab1,"nach",stab2)
    else:
        hanoi(n-1, stab1, stab3, stab2)
        print(n,". Scheibe von",stab1,"nach",stab2)
        hanoi(n-1, stab3, stab2, stab1)
