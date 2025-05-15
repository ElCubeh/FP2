import java.util.Arrays;

public class ArrayTools {
    public static String[] palabrasEnMente(String[] palabras) {
        if (palabras == null) {
            return null;
        }

        String[] resultado = new String[palabras.length];

        for (int i = 0; i < palabras.length; i++) {
            String palabra = palabras[i];
            if (palabra != null && palabra.endsWith("mente")) {
                resultado[i] = palabra.substring(0, palabra.length() - 5); // Eliminar "mente"
            } else {
                resultado[i] = palabra;
            }
        }

        return resultado;
    }

	public static void main (String[] args) {
	    String[] palabras = {"El", "gato", "insolentemente", "saltaba", "ágilmente" };
	    System.out.println(Arrays.toString(palabrasEnMente(palabras)));
	}
}
