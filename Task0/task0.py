<<<<<<< HEAD
import random
spysok=[]
for i in range(30):
    k=random.randint(-100,100)
    spysok.append(k)
print (spysok)
big=spysok[0]
number=0
for nomer in range(len(spysok)):
    if spysok[nomer]>big:
        big=spysok[nomer]
        number=nomer
print ("Найбільший елемент=",big)
print ("Номер найбільшого=",number)
spysok.sort(reverse = True)
print ("Непарні")
for nomer in range(30):
    if spysok[nomer] %2 != 0:
        print (spysok[nomer], end=' ')
        
        
        


        
=======
import random
spysok=[]
for i in range(30):
    k=random.randint(-100,100)
    spysok.append(k)
print (spysok)
big=spysok[0]
number=0
for nomer in range(len(spysok)):
    if spysok[nomer]>big:
        big=spysok[nomer]
        number=nomer
print ("Найбільший елемент=",big)
print ("Номер найбільшого=",number)
spysok.sort(reverse = True)
print ("Непарні")
for nomer in range(30):
    if spysok[nomer] %2 != 0:
        print (spysok[nomer], end=' ')
>>>>>>> 3df249271e92227961e71d0488e53c3e945fd542
