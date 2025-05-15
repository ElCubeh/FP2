import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Functions {
    public static String verbs(String text) {
        if (text == null || text.isEmpty()) {
            return "";
        }
        Pattern pattern = Pattern.compile("\\b\\p{L}+?(o|as|a|amos|áis|an)\\b", Pattern.UNICODE_CASE);
        Matcher matcher = pattern.matcher(text);

        StringBuilder result = new StringBuilder();

        while (matcher.find()) {
            result.append("[").append(matcher.group()).append("]");
        }

        return result.toString();
        
    }
	public static void main (String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.println("Texto a procesar:");
	    String text = input.nextLine();
	    String verbos = verbs(text);
	    System.out.print(verbos);
	}
}
