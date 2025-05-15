public class Main {
    public static void main(String[] args) {
        SteppedCounterCloneable count = new SteppedCounterCloneable(3);
        System.out.println(count.getValue()); // Muestra 0

        for (int i = 0; i < 5; i++) { // Muestra 3 6 9 12 15 en líneas separadas
            count.step();
            System.out.println(count.getValue());
        }

        try {
            SteppedCounterCloneable count1 = (SteppedCounterCloneable) count.clone();
            System.out.println(count1.getValue());  // Muestra 15
        } catch (CloneNotSupportedException e) {
            System.out.println("Error al intentar clonar el objeto");
        }
    }
}