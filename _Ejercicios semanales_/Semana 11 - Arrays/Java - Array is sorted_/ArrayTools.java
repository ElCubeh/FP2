public class ArrayTools {
	// Escriba su código aquí
	public static boolean isSorted (int[] array) {
	    for (int i = 1; i < array.length; i++) {
	        if (array[i] < array[i - 1]) {
	            return false;
	        }
	    }
	    return true;
	}
	public static void main (String[] args) {
	    int[] arrayOfInt = {-10, -8, 1021, 1021, 1040, 2001, 2019};
	    System.out.println(isSorted(arrayOfInt));
	}
}
