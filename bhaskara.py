import math
a = float (input("qual o valor de a?"))
b = float (input("qual o valor e b?"))
c = float (input ("qual o valor de c?"))
delta = (b**2) - 4 * a * c
if a == 0 or delta<0:
     print ("erro")
else: 
     raizdelta = math.sqrt(delta)
     raiz1 = (-b + raizdelta)/2*a
     raiz2 = (-b - raizdelta)/2*a
print (f"a {raiz1} é e a {raiz2} é")



                            
