public class Pruebas {
    public static void main(String[] args) {
        Task t1 = new Task("Lavar los platos", 15);
        Task t2 = new Task("Hacer la compra", 40);
        Task t3 = new Task("Estudiar Java", 120);
        Task t4 = new Task("Ejercicio", 60);
        Task t5 = new Task("Estudiar Python", 150);

        TaskList lista1 = new TaskList();
        TaskList lista2 = new TaskList();

        lista1.addTask(t1);
        lista1.addTask(t2);
        lista1.addTask(t3);
        lista1.addTask(t4);
        lista2.addTask(t5);

        System.out.println("lista1 actual: " + lista1);

        System.out.println("\nTarea en la posición 1: " + lista1.getTask(1)); // Esperado: Hacer la compra: 40 min

        // Tiempo total pendiente
        System.out.println("\nTiempo pendiente: " + lista1.getTimeLeft()); // Esperado: 235

        // Completar tarea en la posición 1
        System.out.println("\nTarea completada (posición 1): " + lista1.taskCompleted(1)); // Esperado: Hacer la compra: 40 min

        // Mostrar lista1 después de completar una tarea
        System.out.println("\nlista1 después de completar una tarea: " + lista1);

        // Tiempo restante y tiempo invertido
        System.out.println("\nTiempo restante: " + lista1.getTimeLeft()); // Esperado: 195
        System.out.println("Tiempo invertido: " + lista1.getTimeSpent()); // Esperado: 40

        // Tarea en posición inválida
        System.out.println("\nIntento de acceder a tarea en posición inválida: " + lista1.getTask(10)); // Esperado: null

        // Completar todas las tareas restantes
        while (lista1.getTimeLeft() > 0) {
            System.out.println("Tarea completada: " + lista1.taskCompleted(0));
        }

        // Estado final
        System.out.println("\nlista1 vacía: " + lista1);
        System.out.println("Tiempo invertido: " + lista1.getTimeSpent()); // Esperado: suma
        System.out.println("Tiempo total invertido: " + TaskList.getTotalTimeSpent()); // Esperado: suma total
        System.out.println("Tarea completada en lista 2: " + lista2.taskCompleted(0));
        System.out.println("Tiempo total invertido: " + TaskList.getTotalTimeSpent()); // Esperado: suma total
    }
}
