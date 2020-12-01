############
#Bubblesort#
############

from random import*

def bubblesort(zahlen):
    for y in range(len(zahlen)):
        for x in range(len(zahlen)-1):
            if (zahlen[x] > zahlen[x+1]):
                zahlen[x], zahlen[x+1] = zahlen[x+1], zahlen[x]
            else:
                pass

######
#Test#
######

zahlen = []
for i in range(10):
    zahlen = zahlen + [randint(1,100)]
print(zahlen)
bubblesort(zahlen)
print(zahlen)