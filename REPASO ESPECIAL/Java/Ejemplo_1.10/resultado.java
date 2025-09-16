/**
 * La clase ErrorLog gestiona un registro de errores de una aplicación.
 * Hereda de LogBase para la funcionalidad básica de la lista enlazada.
 * Añade métodos para resolver, filtrar y contar errores según su prioridad y código.
 */
public class ErrorLog extends LogBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el número de errores que han sido resueltos en ESTE log.
     */
    private int resolvedErrorsCount = 0;

    /**
     * Almacena el número total de errores con prioridad "HIGH" en TODOS los logs.
     * Es 'static' para ser un contador global compartido.
     */
    private static int totalCriticalErrors = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Busca el primer error con un código específico, lo elimina de la lista
     * y actualiza el contador de errores resueltos.
     *
     * @param errorCode El código del error a resolver.
     * @return El objeto AppError resuelto, o null si no se encontró.
     */
    public AppError resolveError(int errorCode) {
        if (first == null) {
            return null; // La lista está vacía.
        }

        // Caso especial: el error a resolver es el primero.
        if (first.value.errorCode == errorCode) {
            AppError errorResolved = first.value;
            first = first.next; // Eliminamos el primer nodo.
            this.resolvedErrorsCount++;
            return errorResolved;
        }

        // Caso general: el error está en el medio o al final.
        Node previous = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.errorCode == errorCode) {
                AppError errorResolved = current.value;
                previous.next = current.next; // Hacemos el "bypass".
                this.resolvedErrorsCount++;
                return errorResolved;
            }
            previous = current;
            current = current.next;
        }

        return null; // El error no fue encontrado.
    }

    /**
     * Devuelve un array con todos los errores que tienen prioridad "HIGH".
     *
     * @return Un array de AppError.
     */
    public AppError[] getHighPriorityErrors() {
        // Primer recorrido: Contar cuántos errores son de alta prioridad.
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.priority.equals("HIGH")) {
                count++;
            }
            current = current.next;
        }

        // Segundo recorrido: Crear el array del tamaño exacto y rellenarlo.
        AppError[] highPriorityErrors = new AppError[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.priority.equals("HIGH")) {
                highPriorityErrors[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return highPriorityErrors;
    }

    /**
     * Cuenta el número de veces que aparece un error con un código específico.
     *
     * @param errorCode El código de error a buscar.
     * @return El número de veces que aparece el error.
     */
    public int countErrorsByCode(int errorCode) {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.errorCode == errorCode) {
                count++;
            }
            current = current.next;
        }
        return count;
    }

    /**
     * Elimina de la lista todos los errores con prioridad "LOW".
     *
     * @return El número de errores de baja prioridad que fueron eliminados.
     */
    public int clearLowPriorityErrors() {
        int deletedCount = 0;

        // Caso especial: eliminar desde el principio de la lista.
        while (first != null && first.value.priority.equals("LOW")) {
            first = first.next;
            deletedCount++;
        }

        // Si la lista no se ha quedado vacía, recorremos el resto.
        if (first != null) {
            Node previous = first;
            Node current = first.next;
            while (current != null) {
                if (current.value.priority.equals("LOW")) {
                    previous.next = current.next;
                    deletedCount++;
                } else {
                    previous = current;
                }
                current = previous.next;
            }
        }
        return deletedCount;
    }
}
