def prim():
	L = []
	for x in range (1,1001):
		zaehler = 0
		for y in range (1,x+1):
			if (x%y == 0):
			    zaehler = zaehler + 1
		        if (zaehler == 2):
			        L = L + [x]
	return(L)

    ###geht nicht###
