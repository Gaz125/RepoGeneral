mensaje = "hola soy emma"
print(f"Mensaje original{mensaje}") 
mayusculas = mensaje.upper 
print(f"Cadena en mayusculas:{mayusculas}") 
print(f"Cadena en minusculas:{mensaje.lower}") 

mensaje2 = " Soy Ema " 
print(f"Cadena sin espacio:{mensaje2.strip}") #eliminar espacios en blanco 

largo_mensaje = len(mensaje) 
print(f"mensaje:{mensaje}")
print(f"Largo del mensaje:{largo_mensaje}")