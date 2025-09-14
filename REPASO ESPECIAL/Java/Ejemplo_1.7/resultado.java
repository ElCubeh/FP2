/**
 * La clase Scheduler gestiona una agenda de eventos para un día.
 * Hereda de SchedulerBase para la funcionalidad básica de la lista enlazada.
 * Añade métodos para cancelar eventos y realizar búsquedas en la agenda.
 */
public class Scheduler extends SchedulerBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena la suma total de las duraciones (en minutos) de todos los eventos
     * en ESTE planificador.
     */
    private int totalMinutesScheduled = 0;

    /**
     * Almacena el número total de eventos cancelados en TODAS las instancias
     * de Scheduler. Es 'static' para ser un contador global compartido.
     */
    private static int totalEventsCancelled = 0;


    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Busca un evento por su nombre, lo elimina de la lista y actualiza los contadores.
     *
     * @param eventName El nombre del evento a cancelar.
     * @return El objeto Event cancelado, o null si no se encontró.
     */
    public Event cancelEvent(String eventName) {
        if (first == null) {
            return null; // La lista está vacía.
        }

        // Caso especial: el evento a cancelar es el primero.
        if (first.value.eventName.equals(eventName)) {
            Event eventCancelled = first.value;
            first = first.next; // Eliminamos el primer nodo.

            // Actualizamos los contadores.
            this.totalMinutesScheduled -= eventCancelled.duration;
            Scheduler.totalEventsCancelled++;

            return eventCancelled;
        }

        // Caso general: el evento está en el medio o al final.
        Node previous = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.eventName.equals(eventName)) {
                Event eventCancelled = current.value;
                previous.next = current.next; // Hacemos el "bypass".

                // Actualizamos los contadores.
                this.totalMinutesScheduled -= eventCancelled.duration;
                Scheduler.totalEventsCancelled++;

                return eventCancelled;
            }
            previous = current;
            current = current.next;
        }

        return null; // El evento no fue encontrado.
    }

    /**
     * Devuelve el tiempo total (en minutos) de todos los eventos programados.
     *
     * @return El total de minutos como un int.
     */
    public int getTotalScheduledTime() {
        return this.totalMinutesScheduled;
    }

    /**
     * Busca y devuelve el primer evento que comienza exactamente a una hora dada.
     *
     * @param time La hora de inicio (formato 24h) a buscar.
     * @return El primer Event que coincida, o null si no hay ninguno.
     */
    public Event findEventAtTime(int time) {
        Node current = first;
        while (current != null) {
            Event event = current.value;
            if (event.startTime == time) {
                return event; // Evento encontrado, lo devolvemos inmediatamente.
            }
            current = current.next;
        }
        return null; // No se encontró ningún evento a esa hora.
    }

    /**
     * Devuelve un array con todos los eventos que comienzan a partir de una hora específica.
     *
     * @param time La hora de referencia.
     * @return Un array de objetos Event cuya hora de inicio es >= time.
     */
    public Event[] getEventsAfter(int time) {
        // Primer recorrido: Contar cuántos eventos cumplen la condición.
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.startTime >= time) {
                count++;
            }
            current = current.next;
        }

        // Segundo recorrido: Crear el array del tamaño exacto y rellenarlo.
        Event[] eventsAfter = new Event[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.startTime >= time) {
                eventsAfter[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return eventsAfter;
    }
}