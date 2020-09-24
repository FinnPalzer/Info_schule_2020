divisor1 = int(input("Bitte geben sie die erste Zahl ein:"))
divisor2 = int(input("Bitte geben sie eine zweite Zahl an:"))
divident = int(input("Bitte geben sie eine Zahl an, die durch die beiden anderen geteilt werden."))

if(divident % divisor1 == 0 and divident % divisor2 == 0  ):
    print("Die Zahl",divident,"ist durch",divisor1,"und",divisor2,"teilbar.")
else:

    if(divident % divisor1 == 0 and divident % divisor2 == 0  ):
        print("Die Zahl",divident,"ist nicht durch",divisor1,"und",divisor2,"teilbar.")
    else:

        if(divident % divisor1 == 0):
            print("Die Zahl",divident,"ist nur durch",divisor1,"teilbar.")
        else:

            if(divident % divisor2 == 0):
                print("Die Zahl",divident,"ist nur durch",divisor2,"teilbar.")
            else: 
                print("Durch Garnix teilbar.")












