import java.util.Scanner;

public class Functions {
	// Escriba aquí su código
	public static int initialVowels(String text) {
        // Lista de vocales, incluyendo mayúsculas, minúsculas, acentuadas y diéresis
        String vowels = "AEIOUÁÉÍÓÚÜaeiouáéíóúü";
        int count = 0;

        if (text != null && !text.isEmpty()) {
            String[] words = text.split("\\s+"); // Separar por espacios (uno o más)

            for (String word : words) {
                if (!word.isEmpty() && vowels.indexOf(word.charAt(0)) != -1) {
                    count++;
                }
            }
        }

        return count;
    }
	public static void main (String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.println("Texto a procesar:");
	    String text = input.nextLine();
	    int nVowels = initialVowels(text);
	    System.out.print("El número de palabras que empiezan por vocal es: " + nVowels);
	}
}
