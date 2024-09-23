public class Producto {
    public static void main(String[] args) {
        String nombreProducto = "Swift";
        System.out.println(nombreProducto);
        double Precio = 2.800 ;
        System.out.println(Precio);
        int cantidadDisponible = 5000;
        System.out.println(cantidadDisponible);
        boolean disponible = true;
        System.out.println(disponible);
    //Imprimir variables
        System.out.println("disponible = " + disponible);
        System.out.println("nombreProducto = " + nombreProducto);
        System.out.println("cantidadDisponible = " + cantidadDisponible);
        System.out.println("Precio = " + Precio);

        //Modificar Valores
         nombreProducto = "Paladini";
         Precio = 2000;
         cantidadDisponible = 0;
         disponible = false;

        System.out.println();

        System.out.println("disponible = " + disponible);
        System.out.println("nombreProducto = " + nombreProducto);
        System.out.println("cantidadDisponible = " + cantidadDisponible);
        System.out.println("Precio = " + Precio);



    }
}
