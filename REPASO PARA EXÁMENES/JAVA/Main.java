import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Main{
    public static void main(String[] args){
        System.out.println("Hola mundo!");
        
        String myString = "Soy una cadena de texto";
        myString = "Aquí cambié la cadena";
        System.out.println(myString);
        final String myConstant = "Esto es una cadena de texto constante";


        int myInt = 69;
        System.out.println(myInt);
        System.out.println(myInt - 33);

        Double myDouble = 3.14;
        System.out.println(myDouble);

        Float myFloat = 6.5f;
        System.out.println(myFloat);

        System.out.println(myDouble + myFloat + myInt + myString);

        Boolean myBoolean = true;
        System.out.println(myBoolean);

        myBoolean = null;
        
        List<String> myList = new ArrayList();
        myList.add(myString);
        myList.add(myInt.toString());
        System.out.println(myList);
        Map<String, String> myMap = new HashMap<>();
        myMap.put("string", myString);
        myMap.put("int", myInt.toString());
        System.out.println(myMap);
        System.out.println(myMap.get("int"));
        for (int i = 0; i < myList.size()M i++) {
            myList.get(i);
        }
        Main myMain = new Main();
        System.out.println(myMain.myFunction(myFirstNumber = 5, mySecondNumber = 6));
    }
    public int myFunction(int myFirstNumber, int mySecondNumber) {
        return myFirstNumber + mySecondNumber;

    }
}