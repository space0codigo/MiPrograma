import json
from datetime import datetime

class Sucursal:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.empleados = []
        self.inventario = []
        self.fecha_creacion = datetime.now().isoformat()
    
    def agregar_empleado(self, nombre, puesto, salario):
        empleado = {
            "nombre": nombre,
            "puesto": puesto,
            "salario": salario
        }
        self.empleados.append(empleado)
        print(f"✓ Empleado {nombre} agregado")
    
    def agregar_producto(self, codigo, nombre, cantidad, precio):
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        self.inventario.append(producto)
        print(f"✓ Producto {nombre} agregado")
    
    def guardar(self, archivo="sucursal.json"):
        datos = {
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "fecha_creacion": self.fecha_creacion,
            "empleados": self.empleados,
            "inventario": self.inventario
        }
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"✓ Datos guardados en {archivo}")
    
    def cargar(self, archivo="sucursal.json"):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.nombre = datos.get("nombre")
                self.direccion = datos.get("direccion")
                self.telefono = datos.get("telefono")
                self.empleados = datos.get("empleados", [])
                self.inventario = datos.get("inventario", [])
            print(f"✓ Datos cargados desde {archivo}")
        except FileNotFoundError:
            print(f"✗ Archivo {archivo} no encontrado")
    
    def mostrar_resumen(self):
        print(f"\n=== SUCURSAL: {self.nombre} ===")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Empleados: {len(self.empleados)}")
        print(f"Productos en inventario: {len(self.inventario)}")

# Ejemplo de uso
if __name__ == "__main__":
    sucursal = Sucursal("Sucursal Centro", "Calle Principal 123", "555-0123")
    
    sucursal.agregar_empleado("Juan Pérez", "Gerente", 2500)
    sucursal.agregar_empleado("María García", "Vendedor", 1800)
    
    sucursal.agregar_producto("P001", "Laptop", 5, 1200)
    sucursal.agregar_producto("P002", "Mouse", 20, 25)
    
    sucursal.mostrar_resumen()
    sucursal.guardar()