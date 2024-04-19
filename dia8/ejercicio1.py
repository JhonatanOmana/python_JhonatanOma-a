precio_suscripcion = 50

class PYTimesUser:
    def _init_(self, nombre, precio_suscripcion=precio_suscripcion):
        self.nombre = nombre
        self.precio_suscripcion = precio_suscripcion
        self.suscripciones = []
        self.valor = 0

    def agregar_suscripcion(self, año):
        self.suscripciones.append(año)

    def suscribir(self, año):
        if año < 1990 or año > 2020:
            print("Lo siento, el año de suscripción debe estar entre 1990 y 2020.")
            return

        if self.valor >= self.precio_suscripcion:
            self.valor -= self.precio_suscripcion
            self.agregar_suscripcion(año)
            print(f"¡Excelente elección! Se ha suscrito al año {año} correctamente.")
            print(f"Dinero restante: {self.valor}")
            regalo = input("¿Desea regalar una suscripción a alguien? (s/n): ")
            if regalo.lower() == 's':
                nombre_otro = input("Por favor, ingrese el nombre de la persona a quien desea regalar: ")
                otro_usuario = PYTimesUser(nombre_otro)
                regalo_año = int(input("Por favor, ingrese el año de suscripción para el regalo: "))
                self.comprar_suscripcion(otro_usuario, regalo_año)
        else:
            print(f"Lo siento, no tienes suficiente dinero ({self.valor}) para comprar la suscripción.")

    def depositar_dinero(self, cantidad):
        self.valor += cantidad

    def comprar_suscripcion(self, otro_usuario, año):
        if self.valor >= otro_usuario.precio_suscripcion:
            self.valor -= otro_usuario.precio_suscripcion
            otro_usuario.agregar_suscripcion(año)
            print(f"¡Has hecho una buena acción! Has comprado una suscripción de regalo para {otro_usuario.nombre} para el año {año}.")
            print(f"Dinero restante: {self.valor}")
        else:
            print(f"Lo siento, no tienes suficiente dinero ({self.valor}) para comprar la suscripción.")

    def obtener_precio_suscripcion(self):
        return self.precio_suscripcion

    def obtener_nombre(self):
        return self.nombre

nombre = input("Hola, ¿cuál es tu nombre?: ")
cel = PYTimesUser(nombre)
cantidad = int(input("Por favor, ingresa la cantidad de dinero que deseas depositar: "))
cel.depositar_dinero(cantidad)

año = int(input("¿A qué año te gustaría suscribirte?: "))
cel.suscribir(año)

print(f"Las suscripciones de {cel.obtener_nombre()}: {cel.suscripciones}")