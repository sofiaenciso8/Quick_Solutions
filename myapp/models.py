from django.db import models
from django.core.exceptions import ValidationError

class Inicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/inicio/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Parqueadero(models.Model):
    factura_diaria = models.CharField(max_length=100)
    factura_mensual = models.CharField(max_length=100)
    reporte_ingresos = models.TextField()
    ticket = models.CharField(max_length=100)
    registro = models.TextField()

    def parqueadero(self, factura_diaria, factura_mensual, reporte_ingresos, ticket, registro):
        self.factura_diaria = factura_diaria
        self.factura_mensual = factura_mensual
        self.reporte_ingresos = reporte_ingresos
        self.ticket = ticket
        self.registro = registro
        self.save()


    def obtener_tipo_pago(self, tipo):
        return f"Tipo de pago realizado: {tipo}"

    def obtener_datos_cliente(self, cliente_id):
        cliente = Cliente.objects.get(id=cliente_id) 
        return cliente

    def buscar_por_registro(self, registro):
       return Parqueadero.objects.filter(registro=registro).first()

    def obtener_comprobante(self, ticket):
      return self.ticket if self.ticket == ticket else None

    def calcular_costo(self):
        horas = 2  
        tarifa_por_hora = 5
        return horas * tarifa_por_hora

    def generar_factura(self):
       factura = f"""
        Factura del parqueadero:
        - Factura diaria: {self.factura_diaria}
        - Factura mensual: {self.factura_mensual}
        - Total Ingresos: {self.reporte_ingresos}
        - Ticket: {self.ticket}
        """
       return factura

    def activar_modo_nocturno(self):
        self.modo_nocturno_activado = True
        return "Modo nocturno activado."

    def agregar_nuevo_cliente(self, cliente):
          nuevo_cliente = Cliente.objects.create(**cliente)
          return nuevo_cliente



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
         self.nombre = nombre
         self.telefono = telefono
         self.contraseña = contraseña
         self.usuario = usuario
         self.rol = 'administrador'
         self.save()
         return f"Administrador {self.nombre} creado con éxito."

    def usuario_nuevo(self, usuario, telefono, contraseña):
         self.usuario = usuario
         self.telefono = telefono
         self.contraseña = contraseña
         self.rol = 'cliente'  
         self.save()
         return f"Usuario {self.usuario} creado con éxito."

    def autorizar_acceso(self):
        if self.rol == 'administrador':
            return True
        else:
            return False

    def acceder_reporte_ingresos(self):
         if self.rol == 'administrador':
            return "Accediendo al reporte de ingresos..."
         else:
            return "No tienes permiso para acceder a este reporte."

    def generar_informe(self):
        if self.rol == 'administrador':
            return "Generando informe de administrador..."
        elif self.rol == 'empleado':
            return "Generando informe de empleado..."
        else:
            return "No tienes permisos para generar informes."

    def eliminar_usuario(self):
        self.delete()
        return f"Usuario {self.usuario} eliminado."

    def suspender_usuario(self):
        self.rol = 'suspendido'
        self.save()
        return f"Usuario {self.usuario} ha sido suspendido."

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    tipo_vehiculo = models.CharField(max_length=20)  

    def agregar_vehiculo(self, placa, tipo_vehiculo):
        if Vehiculo.objects.filter(placa=placa).exists():
            raise ValidationError("La placa ya existe.")
        nuevo_vehiculo = Vehiculo(placa=placa, tipo_vehiculo=tipo_vehiculo)
        nuevo_vehiculo.save()
        return nuevo_vehiculo

    def obtener_placa(self):
        return self.placa


    def obtener_ubicacion(self):
         return "Ubicación no disponible."


class Mapa(models.Model):
    disponibilidad = models.IntegerField()
    ubicacion = models.CharField(max_length=255)

    def mapear(self, num_espacio, disponibilidad, ubicacion):
        self.disponibilidad = disponibilidad
        self.ubicacion = ubicacion
        self.save()  
        return f"Espacio {num_espacio} mapeado en {ubicacion} con disponibilidad {disponibilidad}."

    def obtener_ubicacion(self, ubicacion):
        return self.ubicacion


    def dar_num_espacio(self):
        return self.id

    def dar_disponibilidad(self):
        return self.disponibilidad


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    placa_vehiculo = models.CharField(max_length=10)
    hora_inicial = models.DateTimeField()

    def agregar_cliente(self, nombre, telefono, placa_vehiculo):
        nuevo_cliente = Cliente(nombre=nombre, telefono=telefono, placa_vehiculo=placa_vehiculo)
        nuevo_cliente.save()  
        return nuevo_cliente


    def dar_nombre(self):
        return self.nombre


    def dar_telefono(self):
        return self.telefono

    def dar_placa_vehiculo(self):
        return self.placa_vehiculo

