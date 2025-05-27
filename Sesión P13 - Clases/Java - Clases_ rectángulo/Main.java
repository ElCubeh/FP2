public class Main {
    public static void main(String[] args) {
        Punto[][] tests = {
            { new Punto(2, 3), new Punto(3, 4) },
            { new Punto(0, 0), new Punto(1, 2) }
        };

        for (Punto[] test : tests) {
            Punto p1 = test[0];
            Punto p2 = test[1];

            System.out.println("Puntos " + p1 + " " + p2);
            Rectangulo r = new Rectangulo(p1, p2);
            System.out.println("Perímetro: " + r.perimetro());
            System.out.println("Rectángulo: " + r);
            r.reescalar(1.5);
            System.out.println("Después de reescalar 1.5:");
            System.out.println("Perímetro: " + r.perimetro());
            System.out.println("Rectángulo: " + r);
            System.out.println();
        }
    }
}
