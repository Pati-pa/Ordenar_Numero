# Programa para saber si x es positivo y de 4 digitos

print("------------------------------------------")
print("------------Digite x  y z----------------------")
print("------------------------------------------")

#input
x=int(input("Digite x: "))
y=int(input("Digite y: "))
z=int(input("Digite z: "))

#Procesing
if x < y < z :
    rta= (x , y , z)
else:
    if z < y < x :
        rta= (z , y, x)
    else:
        if x < z < y:
            rta=  (x  , z , y)
        else:
            rta = (y , x , z)

#Outpat
print("------------------------------------------")
print("---------Resultado------------------------")
print("------------------------------------------")
print("Los números ordenados en forma ascendente son: " + str (rta))

