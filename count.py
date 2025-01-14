import string
import sys

def text_analyzer(text=None):

if text is None:
	text = input("Por favor, introduce un texto:")
	
if not isinstance(text, str):
	print("Error: El argumento proporcionado no es unaa cadena de texto.")
	return

mayusculas = 0
minusculas = 0
puntuacion = 0
espacios = 0

for char in text:
	if char.usupper():
		mayusculas += 1
	elif char.islower():
		minusculas += 1
	elif char in string.punctuation:
		puntuacion += 1
	elif char == ' ':
		espacios += 1
		
print(f"Mayusculas: {mayusculas}")
print(f"Minusculas: {minusculas}")
print(f"Signos de puntuacion: {puntuacion}")
print(f"Espacios: {espacios}")
