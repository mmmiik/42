x = (input("Dime un numero: \n"))

if (x != int):
	print("El argumento no es un entero")
else:
	if (x == 0): 
		print("Ese numero es un zero")
	elif (x % 2 == 0):
		print("El numero es par")
	else :
		print("Es impar")
