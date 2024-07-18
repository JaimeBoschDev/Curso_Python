a=[1,2,3,4,5,6]
b=a

print(a)
print(b)

a.append(88)
del a[0]


print(a)
print(b)

#Como puedes observar se hizo el cambio tambien en b
#ES porque utilizan el mismo espacio de memoria
print(id(a))
print(id(b))

#Usamos slice


c= a[:]

a.append(28)
del a[0]

print(a)
print(b)
print(c)

print("a",id(a))
print("b",id(b))
print("c",id(c))