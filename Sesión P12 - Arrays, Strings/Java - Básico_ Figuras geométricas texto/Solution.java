import java.util.Scanner;

public class Solution {
    
    // Escriba aquí los métodos para imprimir las figuras
    public static void printTriangleRectangle (int height) {
        if (height <= 0) return;
        for (int i = 1; i <= height; i++) {
            int stars = 2 * i - 1;
            for (int j = 0; j < stars; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }


    public static void printSquare(int height) {
        if (height <= 0) return;
        int width = 2 * height - 1;
        
        for (int i = 0; i < height; i++) {
            if ( i == 0 || i == height - 1) {
                for (int j = 0; j < width; j++) {
                    System.out.print("*");
                }
            } else {
                System.out.print("*");
                for (int j = 0; j < width - 2; j++) {
                    System.out.print(" ");
                }
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void printPyramid (int height) {
        if (height <= 0) return;
        int maxStars = 2 * height - 1;
        for (int i = 1; i <= height; i++) {
            int stars = 2 * i - 1;
            int spaces = (maxStars - stars) / 2;
            for (int s = 0; s < spaces; s++) {
                System.out.print(" ");
            }
            for (int a = 0; a < stars; a++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduzca un número entero: ");
        int size = scanner.nextInt();
        scanner.close();

        System.out.println("Triángulo Rectángulo:");
        printTriangleRectangle(size);

        System.out.println("\nCuadrado:");
        printSquare(size);

        System.out.println("\nPirámide:");
        printPyramid(size);
    }
}
