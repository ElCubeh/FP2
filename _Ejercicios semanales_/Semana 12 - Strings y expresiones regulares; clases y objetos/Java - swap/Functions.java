import java.util.Scanner;

public class Functions {
	// Escriba aquí su código
	public static String swap(String text) {
        if (text == null || text.trim().isEmpty()) {
            return "";
        }

        String[] words = text.trim().split("\\s+");
        StringBuilder result = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--) {
            String word = words[i];
            if (!word.isEmpty()) {
                // Capitalizar: primera letra en mayúscula, resto en minúscula
                String capitalized = word.substring(0, 1).toUpperCase() +
                                     word.substring(1).toLowerCase();
                result.append(capitalized);
                if (i > 0) {
                    result.append(" ");
                }
            }
        }

        return result.toString();
    }
	public static void main (String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.println("Texto a procesar:");
	    String text = input.nextLine();
	    String swapped = swap(text);
	    System.out.print(swapped);
	}
}
