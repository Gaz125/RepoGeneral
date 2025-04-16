from random import randint
nombre = input("Ingrese su nombre") 
apellido = input ("Ingrese su apellido")
nacimiento = input ("Ingrese su año de nacimiento (aaaa)")

nombre_2 = nombre.strip ().upper ()[0:2] 
apellido_2 = apellido.strip ().upper ()[0:2] 
nacimiento_2 = nacimiento.strip ()[2:3] 

aleatorio = randint(1000,9999)

id_unico = f'{nombre_2}{apellido_2}{nacimiento_2}{aleatorio}' 

print (f"""/n Hola{nombre},
       Tu Id generado es: {id_unico}
       """)
