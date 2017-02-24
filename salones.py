

class Espacio:

    nombre = ""
    numero = 0

    def __init__(self,nombre, numero, capacidad):
        self.nombre = nombre
        self.numero = numero
        self.capacidad = capacidad

class Salon(Espacio):

    capacidad = 0

s1 = Salon("Salon 1", 1, 11)
s2 = Salon("Salon 2", 2, 15)
s3 = Salon("Salon 3", 3, 15)
s4 = Salon("Salon 4", 4, 17)
s5 = Salon("Salon 5", 5, 10)
s6 = Salon("Salon 6", 6, 5)
s7 = Salon("Salon 7", 7, 9)
s8 = Salon("Salon 8", 8, 20)
s9 = Salon("Salon 9", 9, 12)
s10 = Salon("Salon 10", 10, 13)
lectura = Espacio("Estacion de Lectura", 11, 100)

print "Nombre: %s" %s1.nombre
print "Numero: %s" %s1.numero
print "Capacidad: %s" %lectura.capacidad

print dir(s1)


#jorosas@gmail.com
