public class OddEven {
	// Escriba aquí su código
	public static boolean isOdd(int number) {
        return number % 2 != 0;
    }
	public static void main (String[] args) {
	    for (int i = 0; i < 10; i++) {
	        if (isOdd(i)) {
	            System.out.println(i + " es impar");
	        } else {
	            System.out.println(i + " es par");
	        }
	    }
	}
}
