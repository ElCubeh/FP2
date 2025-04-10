import java.util.Scanner;

class Area {
    /**
     * Muestra el área de un rectángulo.
     */
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);

        // Escriba aquí su código
        System.out.print("Base: ");
        int base = input.nextInt();

        System.out.print("Altura: ");
        int altura = input.nextInt();

        int area = base * altura;
        System.out.println(area);
    }
}