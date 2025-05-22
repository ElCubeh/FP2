import java.util.Scanner;

public class Solution {
    //Escriba aquí isPalindrome
    public static boolean isPalindrome(int num) {
        if (num < 0) {
            return false;
        }
        int originalNum = num;
        int reversedNum = 0;
        while (num > 0) {
            int lastDigit = num % 10;
            reversedNum = reversedNum * 10 + lastDigit;
            num = num / 10;
        }
        return originalNum == reversedNum;
    }

    //Escriba aquí countPalindromes
    public static int countPalindromes(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                count++;
            } 
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduzca un número entero: ");
        int n = scanner.nextInt();
        scanner.close();
        System.out.println(isPalindrome(n));
        System.out.println(countPalindromes(n));
    }
}
