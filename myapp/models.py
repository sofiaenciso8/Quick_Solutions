from django.db import models


class Parqueadero(models.Model):
    factura_diaria = models.CharField(max_length=100)
    factura_mensual = models.CharField(max_length=100)
    reporte_ingresos = models.TextField()
    ticket = models.CharField(max_length=100)
    registro = models.TextField()

    def parqueadero(self, factura_diaria, factura_mensual, reporte_ingresos, ticket, registro):
        pass

    def obtener_tipo_pago(self, tipo):
        pass

    def obtener_datos_cliente(self, cliente_id):
        pass

    def obtener_reaches_financiera(self):
        pass

    def buscar_por_registro(self, registro):
        pass

    def obtener_comprobante(self, ticket):
        pass

    def calcular_costo(self):
        pass

    def generar_factura(self):
        pass

    def activar_modo_nocturno(self):
        pass

    def agregar_nuevo_cliente(self, cliente):
        pass



class Usuario(models.Model):
    ROLES = (
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
        ('cliente', 'Cliente'),
    )

    usuario = models.CharField(max_length=100)
    telefono = models.IntegerField()
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)

    def administrador(self, nombre, telefono, contraseña, usuario):
        pass

    def usuario_nuevo(self, usuario, telefono, contraseña):
        pass

    def autorizar_acceso(self):
        pass

    def acceder_reporte_ingresos(self):
        pass

    def generar_informe(self):
        pass

    def eliminar_usuario(self):
        pass

    def suspender_usuario(self):
        pass

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    tipo_vehiculo = models.CharField(max_length=20)  # Ejemplo: Carro, Moto, etc.

    def agregar_vehiculo(self, placa, tipo_vehiculo):
        pass

    def obtener_placa(self):
        pass

    def obtener_ubicacion(self):
        pass

class Mapa(models.Model):
    disponibilidad = models.IntegerField()
    ubicacion = models.CharField(max_length=255)

    def mapear(self, num_espacio, disponibilidad, ubicacion):
        pass

    def obtener_ubicacion(self, ubicacion):
        pass

    def dar_num_espacio(self):
        pass

    def dar_disponibilidad(self):
        pass


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    placa_vehiculo = models.CharField(max_length=10)
    hora_inicial = models.DateTimeField()

    def agregar_cliente(self, nombre, telefono, placa_vehiculo):
        pass

    def dar_nombre(self):
        pass

    def dar_telefono(self):
        pass

    def dar_placa_vehiculo(self):
        pass