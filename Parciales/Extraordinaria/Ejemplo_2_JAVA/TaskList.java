// Desarrolle aquí su código

/**
 * La clase TaskList gestiona una lista enlazada de objetos Task (tareas).
 * Extiende de una clase base TaskListBase (cuyo código no se muestra aquí)
 * y añade funcionalidades para gestionar el tiempo dedicado a las tareas.
 */
public class TaskList extends TaskListBase {
    
    // Variable de clase (estática) para almacenar el tiempo total invertido
    // en tareas de TODAS las instancias de TaskList que se creen.
    // Al ser 'static', es compartida por todos los objetos de esta clase.
    private static int totalTimeSpent = 0;
    
    // Variable de instancia para almacenar el tiempo invertido en las tareas
    // completadas de ESTA lista en particular.
    private int timeSpent = 0;
    
    /**
     * Constructor por defecto.
     * Llama al constructor de la clase padre (TaskListBase) para inicializar
     * la lista.
     */
    public TaskList() {
        super(); // Llama al constructor de TaskListBase
    }

    /**
     * Marca una tarea como completada, la elimina de la lista y actualiza los contadores de tiempo.
     * @param index El índice de la tarea a completar en la lista.
     * @return La tarea que ha sido completada y eliminada. Devuelve null si el índice no es válido.
     */
    public Task taskCompleted(int index) {
        // Comprueba si el índice está fuera de los límites de la lista.
        if (index < 0 || index >= size) {
            return null; // Índice inválido, no se hace nada.
        }

        // Nodos para recorrer la lista. 'prev' apunta al nodo anterior a 'current'.
        Node prev = null;
        Node current = head; // 'head' es el primer nodo de la lista (heredado de TaskListBase).
        int pos = 0; // Contador para la posición actual.

        // Recorre la lista hasta encontrar el nodo en la posición 'index'.
        while (current != null && pos < index) {
            prev = current;
            current = current.next;
            pos++;
        }

        // Si 'current' es null, algo fue mal (no debería pasar si la comprobación inicial es correcta).
        if (current == null) {
            return null;
        }

        // --- Eliminar el nodo de la lista ---
        if (prev == null) {
            // Si 'prev' es null, significa que el nodo a eliminar es el primero (head).
            head = current.next;
        } else {
            // Si es un nodo intermedio o el último, se enlaza el anterior con el siguiente.
            prev.next = current.next;
        }
        size--; // Decrementa el tamaño de la lista (variable heredada de TaskListBase).

        // --- Actualizar tiempos ---
        // Guarda la tarea completada para obtener su duración.
        Task completedTask = current.data;
        // Suma el tiempo de la tarea completada al contador de esta lista.
        timeSpent += completedTask.getTime();
        // Suma el tiempo de la tarea completada al contador global (estático).
        totalTimeSpent += completedTask.getTime();

        // Devuelve la tarea que se acaba de completar.
        return completedTask;
    }

    /**
     * Calcula y devuelve el tiempo total estimado para completar todas las tareas
     * restantes en ESTA lista.
     * @return La suma de los tiempos de todas las tareas pendientes en la lista.
     */
    public int getTimeLeft() {
        int total = 0;
        Node current = head; // Empieza desde el primer nodo.
        // Recorre toda la lista.
        while (current != null) {
            // Suma el tiempo de cada tarea al total.
            total += current.data.getTime();
            current = current.next; // Avanza al siguiente nodo.
        }
        return total;
    }

    /**
     * Devuelve el tiempo total invertido en las tareas ya completadas de ESTA lista.
     * @return El valor de la variable de instancia 'timeSpent'.
     */
    public int getTimeSpent() {
        return timeSpent;
    }

    /**
     * Método estático que devuelve el tiempo total invertido en tareas de TODAS
     * las listas de tareas creadas.
     * @return El valor de la variable de clase 'totalTimeSpent'.
     */
    public static int getTotalTimeSpent() {
        return totalTimeSpent;
    }

    /**
     * Convierte la lista enlazada de tareas en un array de tipo Task.
     * @return Un array que contiene todas las tareas actualmente en la lista.
     */
    public Task[] getTaskArray() {
        // Crea un array con el tamaño actual de la lista.
        Task[] tasks = new Task[size];
        Node current = head; // Empieza desde el primer nodo.
        int i = 0; // Índice para el array.
        // Recorre la lista enlazada.
        while (current != null) {
            // Asigna la tarea del nodo actual a la posición correspondiente en el array.
            tasks[i++] = current.data;
            current = current.next; // Avanza al siguiente nodo.
        }
        return tasks;
    }
}