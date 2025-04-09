import java.util.Scanner;
public class Desafio8 {

    public class PromedioCalificaciones {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            int cantidad;
            double suma = 0;

            System.out.print("¿Cuántas calificaciones desea promediar?: ");
            cantidad = scanner.nextInt();

            for (int i = 1; i <= cantidad; i++) {
                System.out.print("Ingrese la calificación #" + i + ": ");
                double calificacion = scanner.nextDouble();
                suma += calificacion;
            }

            if (cantidad > 0) {
                double promedio = suma / cantidad;
                System.out.println("El promedio de las calificaciones es: " + promedio);
            } else {
                System.out.println("No se ingresaron calificaciones válidas.");
            }

            scanner.close();
        }
    }
}
