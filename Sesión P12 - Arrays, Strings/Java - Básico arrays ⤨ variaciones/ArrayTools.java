import java.util.Arrays;

public class ArrayTools {
	// Escriba aquí su código
	public static int[] procesar(String[] v1, String[] v2) {
	    int len = Math.min(v1.length, v2.length);
	    int[] resultado = new int[len];
	    for (int i = 0; i < len; i++){
	        if (v1[i].compareTo(v2[i]) >= 0) {
	            resultado[i] = v1[i].length();
	        } else {
	            resultado[i] = v2[i].length();
	        }
	    }
	    return resultado;
	}
}
