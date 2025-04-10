import java.util.Scanner;

public class Main {
    // Escriba aquí su código
    public static void showNumbers(int inf, int sup) {
        if (inf <= sup) {
            for (int i = inf; i <= sup; i++) {
                System.out.println(i);
            }
        }
    }
    
    public static void main(String[] args) {
         Scanner input = new Scanner(System.in);
         System.out.print("primer número : ");
         int inf = input.nextInt();
         System.out.print("segundo número: ");
         int sup = input.nextInt();
         showNumbers(inf, sup);
    }
}
