public class Pruebas {
    public static void main(String[] args) {
        InterestGroup group1 = new InterestGroup();
        InterestGroup group2 = new InterestGroup();

        System.out.println("Inicialmente:");
        System.out.println(group1); // ➡️ null
        System.out.println(group2); // ➡️ null

        // Añadimos miembros al primer grupo
        group1.addMember("Ana");
        group1.addMember("Luis");
        group1.addMember("Marta");

        System.out.println("\nGrupo 1 tras añadir miembros:");
        System.out.println(group1); // ➡️ [Marta]->[Luis]->[Ana]->null

        // Añadimos miembros al segundo grupo
        group2.addMember("Luis");
        group2.addMember("Carlos");
        group2.addMember("Elena");

        System.out.println("\nGrupo 2 tras añadir miembros:");
        System.out.println(group2); // ➡️ [Elena]->[Carlos]->[Luis]->null

        // Comprobamos si ciertos miembros están en los grupos
        System.out.println("\nComprobación de miembros:");
        System.out.println("Luis en grupo1: " + group1.isMember("Luis")); // true
        System.out.println("Carlos en grupo1: " + group1.isMember("Carlos")); // false
        System.out.println("Elena en grupo2: " + group2.isMember("Elena")); // true

        // Tamaño de los grupos
        System.out.println("\nTamaño de los grupos:");
        System.out.println("Grupo1: " + group1.getSize()); // 3
        System.out.println("Grupo2: " + group2.getSize()); // 3

        // Unión de grupos
        InterestGroup unionGroup = group1.union(group2);
        System.out.println("\nUnión de grupo1 y grupo2:");
        System.out.println(unionGroup); // ➡️ [Ana]->[Luis]->[Marta]->[Carlos]->[Elena]->null

        // Probar que no se agregan duplicados
        group1.addMember("Luis"); // Ya está
        System.out.println("\nGrupo1 tras intentar añadir a 'Luis' otra vez:");
        System.out.println(group1); // ➡️ [Ana]->[Luis]->[Marta]->null

        // Probar que se eliminan miembros
        group1.removeMember("Marta");
        System.out.println("\nGrupo1 tras eliminar 'Marta':");
        System.out.println(group1); // ➡️ [Ana]->[Luis]->null
    }
}
