import java.util.Scanner;


public class perimetro {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Base: ");
        int base = input.nextInt();

        System.out.print("Altura: ");
        int altura = input.nextInt();

        int perimetro = 2 * (base + altura);
        System.out.println("Perímetro: " + perimetro);

    }
}
