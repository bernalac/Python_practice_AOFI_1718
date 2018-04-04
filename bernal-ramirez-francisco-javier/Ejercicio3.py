var_numero1 = 0
var_numero2 = 0
var_numero3 = 0
print("Dime un número mayor que cero")
var_numero1=int(input())
if var_numero1 > 0:
		print("Dime un número mayor que el anterior")
		var_numero2=int(input())
		if var_numero2 > var_numero1:
			print("Dime un número menor que 0")
			var_numero3=int(input())
			if var_numero3 < 0:
				print(var_numero1,"+",var_numero2,"+",var_numero3,"=",var_numero1+var_numero2+var_numero3)
