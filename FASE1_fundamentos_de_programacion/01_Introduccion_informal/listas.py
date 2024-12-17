# Las Listas

## tipo compuesto de dato que puede almacenar distintos
# valores (llamdos items) ordenados entre [] y separados por comas

numeros = [1,2,3,4]

print(numeros)

datos = [4, "una cadena", -15,3.14, "otra cadena"]
print(datos)


#indices y Slicing
#funciona de una forma muy similar a las cadenas de caracteres 

datos = datos[-2:]
print(datos)

#sumar listas
# da resultado una lista que incluye 
# todos los items

numeros = numeros + [5,6,7,8]
print(numeros)

# son modificables
pares = [0,2,4,5,8,10]
pares[3]=6
print(pares)

# .append() sirve para añadir un item al final
#de la lista

pares.append(12)
print(pares)

pares.append(7*2)
print(pares)

letras = ['a','b','c','d','e','f']
letritas = letras[:3]
print(letritas)

letras[:3] = ['A','B','C']
print(letras)

letras[:3] = []
print(letras)


# funcion lenn()

letras = []
len(letras)
print(letras)

# Listas Anidadeas

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print(r)

sub = r[0] # primer sublista
print(sub)

sub = r[-1] # ultima sublista
print(sub)

sub = r[0][0] # primera sublista y de ella el primer item
print(sub)

sub = r[1][1] # primera sublista y de ella el primer item
print(sub)

sub = r[2][2] # primera sublista y de ella el primer item
print(sub)

sub = r[-1][-1] # primera sublista y de ella el primer item
print(sub)