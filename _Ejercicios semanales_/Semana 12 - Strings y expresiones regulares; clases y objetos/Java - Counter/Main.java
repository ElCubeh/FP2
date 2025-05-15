public class Main {
    public static void main(String[] args) {
        Counter count = new Counter();
        System.out.println(count.getValue());

        for (int i = 0; i < 5; i++) {
            count.step();
            System.out.println(count.getValue());
        }
        
        count.reset();
        System.out.println(count.getValue());
    }
}