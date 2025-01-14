string = input("Dime cualquier frase.\n")

cadenaInvertida = string[::-1] #string mi variable donde guardo el input para saber la frase 
			       #[::-1] gira la frase 
x = cadenaInvertida.swapcase() #creo una nueva variable que almacena cadena invertida y la convierte de may'usculas a min'usculas y viceversa

print(x) # p de print
