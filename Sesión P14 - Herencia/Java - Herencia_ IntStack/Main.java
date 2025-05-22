/**
 * Puede modificar main si quiere probar cosas diferentes con el COHETE
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("(Ejecución del fichero modificable Main.java)");
        IntStack stack = new IntStack(10);
        try {
            for (int i = 0; i < 9; i++) stack.insert(i * 3);
           
            System.out.println(stack);
            System.out.println(stack.equals(stack));
       
            stack.insert(99);
            stack.insert(100);
        } catch (CapacityOverflow e) {
            System.out.println(e.getMessage());
            System.out.println(stack);
        }
    }
}
