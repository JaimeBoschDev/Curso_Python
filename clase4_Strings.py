#Manipulación de Cadenas de Texto en Python

_Nombre_ ="Jaime"
_Apellido_='Gonzalez Bosch'
_NombreCompleto_ ='''Jaime Joaquin
Gonzlaez Bosch '''

print(_Nombre_)
print(_Apellido_)
print(_NombreCompleto_)


print(type(_Nombre_))
print(type(_Apellido_))
print(type(_NombreCompleto_))

#Todas son de tipo String

#Podemos obtener como cada letra si lo usamos como array
# 

print(_Nombre_[0])
print(_Nombre_[1])
print(_Nombre_[2])

#Podemos ir de la ultima al inicio si ponemos numero negativos
#-1 Sería la ultima, -2 la antepenultima, etc 

print(_Nombre_[-1])
print(_Nombre_[-2])

#Concatenación
print(_Nombre_ + " " + _Apellido_)

#Obtener el numero de caracteres
print(len(_NombreCompleto_))

#Convertir a minusculas
print(_NombreCompleto_.lower())

#Convertir a mayusculas
print(_NombreCompleto_.upper())