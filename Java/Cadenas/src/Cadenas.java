public class Cadenas {
    public static void main(String[] args) {
        //Manejo de Cadenas 
        var cadena1= "Hola";
        System.out.println("cadena1 = " + cadena1);
       var cadena2 = new String ("Mundo");
        System.out.println("cadena2 = " + cadena2);

        var cadena3= cadena1 +" "+cadena2;
        // Cadena multiples lineas
        var cadena4 = """
                Hola
                soy 
                Ema
                """;
    }
}
