#Clase 2 
print("Hola mundo".title())

texto = "Pancho#$Pantera#$panchopantera@gmail.com" # <- Todo lo que esté marcado abajo se va a borrar

persona = texto.split('#$') # <- Lo que está entre comillas va a aparecer distinto a la hora de mostrar lo que está escrito 

print(persona)

print(persona[1]) # <- Si muestro un solo elemento de la lista por ende me mostraria en este caso "Pantera" ya que seria (pancho(0) , pantera(1) , mail(2))

#texto2 = "=".join(persona)  # <- Concateno los elementos de la lista con iguales(=)
#print(texto2)

print("=".join(persona)) # <- Lo mismo de arriba pero en el mismo print

print("hola mundo".replace("mundo","SEXO")) # <- Lo primero que está entre comillas es reemplazado por lo de al lado, en este caso quedaría "hola SEXO"

#print("hola mundo".replace("o","SEXO")) <- Lo mismo pero en vez de reemplazar la palabra mundo reemplazo directamente la letra o

print("hola mundo".replace("mundo","/""")) 
print("hola mundo".replace("mundo","//")) 

print("Nombre: {0}".format(persona[0]))
#ES LO MISMO QUE PONER PRINT(F'NOMBRE: {PERSONA[0]}')

