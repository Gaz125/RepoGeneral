import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner consola = new Scanner(System.in);
        //Aplicacion Calculadora
        System.out.println("****Aplicacion Calculadora****");
        //Menu
        System.out.println("""
                1.Suma
                2.Resta
                3.Multiplicacion
                4.Division
                5.Salir
                
                
               
                """);
        System.out.println("Realice una operacion");
        var operacion = Integer.parseInt (consola.nextLine());

        //Ingresar valores validos
        if(operacion >=1 && operacion<=4);
        { System.out.println("Proporcionar valor operacion1");

            var operacion1 =  Integer.parseInt( consola.nextLine());
            System.out.println("Proporcionar valor operacion2");
            var operacion2 = Integer.parseInt( consola.nextLine());
            int resultado;
            switch (operacion){
                case 1 ->{
                    resultado = operacion1 + operacion2;
                    System.out.println("Resultado Suma:"+ resultado);
                }
                case 2 ->{
                    resultado = operacion1-operacion2;
                    System.out.println("Resultado Resta:"+ resultado);
                }
                case 3 ->{
                    resultado = operacion1*operacion2;
                    System.out.println("Resultado Multiplicacion:"+ resultado);
                }
                case 4 ->{
                    resultado =operacion1/operacion2;
                    System.out.println("Resultado Division:"+ resultado);
                }
                default ->
                    System.out.println("Error de:"+operacion);

            }

        }


        }

    }







