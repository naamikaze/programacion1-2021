#Este es el de la clase
def decifrar(clave):
    clave1='' #Declaro que esto es texto y no numero, por lo cual cuando le sume algo se agrega ahí no se modifica el valor.
    clave2=''
    for i in range(len (clave)):
        if ((i + 1) % 2 == 0): #Cambio el significado del indice para que la primera posicion sea el 1
            #Basicamente mantiene la misma posicion, pero cuando hago la lógica hago como si valiera mas

            clave2+=clave[i] #Al meter += estoy haciendo que le agregue eso a lo anterior así no se reemplaza.
        else:
            clave1+=clave[i]
    return clave1, clave2

print(decifrar('18293'))

#String sería texto ""
#Int es numero 