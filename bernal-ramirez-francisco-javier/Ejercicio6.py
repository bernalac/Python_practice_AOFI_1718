var_numero = 0

print ("Dime un numero y te dire si es par/impar y multiplo de 3")
var_numero=int(input())
if var_numero %2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")
if var_numero %3 == 0:
    print ("Este numero es multiplo de 3")
else:
    print ("Este numero no es multiplo de 3")
