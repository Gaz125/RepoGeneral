import json
import os
import datetime
from plyer import notification

FILE_NAME = "cumpleaños.json"

def cargar_cumpleaños():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def guardar_cumpleaños(cumpleaños):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(cumpleaños, file, indent=4, ensure_ascii=False)

def agregar_cumpleaños():
    nombre = input("Nombre: ")
    fecha = input("Fecha de cumpleaños (DD-MM-YYYY): ")
    cumpleaños = cargar_cumpleaños()
    cumpleaños[nombre] = fecha
    guardar_cumpleaños(cumpleaños)
    print(f"Cumpleaños de {nombre} agregado correctamente.")

def buscar_cumpleaños():
    nombre = input("Ingrese el nombre a buscar: ")
    cumpleaños = cargar_cumpleaños()
    if nombre in cumpleaños:
        print(f"El cumpleaños de {nombre} es el {cumpleaños[nombre]}.")
    else:
        print("No se encontró el cumpleaños de esa persona.")

def eliminar_cumpleaños():
    nombre = input("Ingrese el nombre a eliminar: ")
    cumpleaños = cargar_cumpleaños()
    if nombre in cumpleaños:
        del cumpleaños[nombre]
        guardar_cumpleaños(cumpleaños)
        print(f"Cumpleaños de {nombre} eliminado correctamente.")
    else:
        print("No se encontró el cumpleaños de esa persona.")

def notificar_cumpleaños():
    hoy = datetime.datetime.today().strftime("%d-%m-%Y")
    cumpleaños = cargar_cumpleaños()
    for nombre, fecha in cumpleaños.items():
        if fecha == hoy:
            notification.notify(
                title="¡Feliz Cumpleaños!",
                message=f"Hoy es el cumpleaños de {nombre}!",
                timeout=10
            )

def mostrar_menu():
    notificar_cumpleaños()
    while True:
        print("\nGestor de Cumpleaños")
        print("1. Agregar cumpleaños")
        print("2. Buscar cumpleaños")
        print("3. Eliminar cumpleaños")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_cumpleaños()
        elif opcion == "2":
            buscar_cumpleaños()
        elif opcion == "3":
            eliminar_cumpleaños()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
