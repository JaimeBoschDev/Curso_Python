# Creación de listas
lista_vacia = []
lista_numeros = [3, 99, 1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)

# Acceder a elementos
print("nAcceso a elementos")
print("Primer elemento:", lista_numeros[0])
print("Último elemento:", lista_numeros[-1])

# Modificar elementos
print("nModificar elementos")
lista_numeros[0] = 10
print("Lista de números modificada:", lista_numeros)

# Agregar y eliminar elementos
print("nAgregar y eliminar elementos")
lista_numeros.append(6) #Lo agrega hasta el final
print("Lista después de append:", lista_numeros)
lista_numeros.insert(2, 99) #Lo agrega en la posición 2
print("Lista después de insert:", lista_numeros)
lista_numeros.remove(99) #Elimina el primero que encuentra
print("Lista después de remove:", lista_numeros)
ultimo = lista_numeros.pop() #Elimina el ultimo
print("Elemento eliminado con pop:", ultimo)
print("Lista después de pop:", lista_numeros)
elemento = lista_numeros.pop(1) #Elimina la posición que quieres
print("Elemento eliminado en la posición 1:", elemento)
print("Lista después de eliminar en la posición 1:", lista_numeros)

# Operaciones básicas
print("nOperaciones básicas")
lista_concatenada = lista_numeros + lista_mixta
print("Lista concatenada:", lista_concatenada)
lista_repetida = lista_numeros * 2
print("Lista repetida:", lista_repetida)
print("¿Está 3 en la lista?", 3 in lista_numeros) #Validación con In 3 in [Lista]
print("Longitud de la lista:", len(lista_numeros)) #Obtener la longitud

i=0
for elemento in lista_numeros:
    i = i+ 1
    print("Elemento de la lista "+ str(i) +" => " ,elemento)
