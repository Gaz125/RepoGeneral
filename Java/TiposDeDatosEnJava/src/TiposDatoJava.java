public class TiposDatoJava {
    public static void main(String[] args) {
        //Enteros 
        byte tipoByte=127;
        System.out.println("tipoByte = " + tipoByte); 
        short tipoShort = 32000;
        System.out.println("tipoShort = " + tipoShort); 
        int tipoInt = 2147483647;
        System.out.println("tipoInt = " + tipoInt);
        long tipoLong = 123123233L;
        System.out.println("tipoLong = " + tipoLong); 
        
        //Tipo flotante 
        float tipoFloat = 2.15F;
        System.out.println("tipoFloat = " + tipoFloat); 
        double tipoDouble = 3.23345;
        System.out.println("tipoDouble = " + tipoDouble);

        //Caracter
        char tipoChar = 'A';
        System.out.println("tipoChar = " + tipoChar); 
        tipoChar = 65 ;
        System.out.println("tipoChar = " + tipoChar); 
        tipoChar = '@';
        System.out.println("tipoChar = " + tipoChar); 
        
        //Boolean 
        boolean tipoBoolean = true ;
        System.out.println("tipoBoolean = " + tipoBoolean);
        tipoBoolean = false ;
        System.out.println("tipoBoolean = " + tipoBoolean);

        //Tipo Objeto
        String nombre = null;
        System.out.println("nombre = " + nombre); 
        nombre ="Emma";
        System.out.println("nombre = " + nombre);


    }
}
