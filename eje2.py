tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

lower=[]
greater=[]

number=int(input("ingrese numero: "))

for i in tam:
  name, space, tupla=i.partition(" ") 
  x=int(tupla.split(",")[0])
  y=int(tupla.split(",")[1]) 
  if x>=number: 
    greater.append([name,(x,y)])
  else:
    lower.append([name,(x,y)])

print("imagenes con con primer cooordenada mayor o igual: " ,greater)
print("imagenes con primer coordenada menor: " , lower)