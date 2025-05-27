public class Main {
    public static void main(String[] args) {
        Rational r1 = new Rational(2, 3);
        Rational r2 = new Rational(1, 6);
        
        System.out.println("r1: " + r1);  // 2 / 3
        System.out.println("r2: " + r2);  // 1 / 6

        System.out.println("Suma: " + r1.add(r2));      // 5 / 6
        System.out.println("Multiplicación: " + r1.prod(r2)); // 1 / 9

        System.out.println("¿r1 es igual a r2?: " + r1.equals(r2)); // false
    }
}
