public class Main {
    public static void main(String[] args) {
        SteppedCounter count = new SteppedCounter(3);
        System.out.println(count.getValue()); // Muestra 0

        for (int i = 0; i < 5; i++) {         // Muestra 3 6 9 12 15 en líneas separadas
            count.step();
            System.out.println(count.getValue());
        }


        count.reset();
        System.out.println(count.getValue());  // Muestra 0
    }
}