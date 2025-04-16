empleado = input("Escriba su nombre: ") 
edad_empleado = input ("Escriba su edad: ") 
salario = input("Cual es el salario del empleado: ") 
jefe_seccion = input("Es jefe de Seccion? (Si/No)") 

#Convertir a booleano 

jefe_seccion = jefe_seccion.lower() == "Si" 

#Imprimir datos del empleado. 
print("\nDatos del empleado") 
print(f"Nombre:{empleado}") 
print(f"Edad:{edad_empleado}") 
print(f"Salario:{salario:.2f}") 
print(f"Es jefe de Secccion:{jefe_seccion}")