import java.util.Scanner;


class Suma {
    /**
     * main method sums to ints
     */ 
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);

        // Escriba aquí su código
         System.out.print("Dame un número entero: ");
        int num1 = input.nextInt();

        System.out.print("Dame otro número entero: ");
        int num2 = input.nextInt();

        int suma = num1 + num2;
        System.out.println("La suma es: " + suma);
    }
}