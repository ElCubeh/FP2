// Desarrolle aquí su código
public class TaskList extends TaskListBase {
    
    // Variable de clase para el tiempo total de TODAS las listas
    private static int totalTimeSpent = 0;
    
    // Tiempo dedicado en ESTA lista
    private int timeSpent = 0;
    
    public TaskList() {
        super();
    }

    public Task taskCompleted(int index) {
        if (index < 0 || index >= size) {
            return null;
        }

        Node prev = null;
        Node current = head;
        int pos = 0;

        while (current != null && pos < index) {
            prev = current;
            current = current.next;
            pos++;
        }

        if (current == null) {
            return null; // índice fuera de rango
        }

        // Eliminar el nodo
        if (prev == null) {
            head = current.next;
        } else {
            prev.next = current.next;
        }
        size--;

        // Actualizar tiempos
        Task completedTask = current.data;
        timeSpent += completedTask.getTime();
        totalTimeSpent += completedTask.getTime();

        return completedTask;
    }

    public int getTimeLeft() {
        int total = 0;
        Node current = head;
        while (current != null) {
            total += current.data.getTime();
            current = current.next;
        }
        return total;
    }

    public int getTimeSpent() {
        return timeSpent;
    }

    public static int getTotalTimeSpent() {
        return totalTimeSpent;
    }

    public Task[] getTaskArray() {
        Task[] tasks = new Task[size];
        Node current = head;
        int i = 0;
        while (current != null) {
            tasks[i++] = current.data;
            current = current.next;
        }
        return tasks;
    }
}
