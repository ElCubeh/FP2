/**
 * La clase Inbox gestiona una bandeja de entrada de correos electrónicos.
 * Hereda de InboxBase para la funcionalidad básica de la lista.
 * Añade métodos para marcar correos como leídos, borrarlos y buscarlos.
 */
public class Inbox extends InboxBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el número de correos no leídos en ESTA bandeja de entrada.
     */
    private int unreadCount = 0;

    /**
     * Almacena el número total de correos marcados como spam y eliminados
     * en TODAS las instancias de Inbox. Es 'static' y compartido globalmente.
     */
    private static int totalSpamDeleted = 0;


    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Marca un correo como leído, buscándolo por su posición (índice).
     * Si el correo no estaba leído, actualiza el contador de no leídos.
     *
     * @param index La posición del correo a marcar como leído.
     * @return El objeto Email modificado, o null si el índice es inválido.
     */
    public Email markAsRead(int index) {
        if (index < 0 || index >= getSize()) {
            return null; // Índice inválido.
        }

        // Encontramos el nodo en la posición 'index'.
        Node current = first;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }

        Email emailToRead = current.value;

        // Si el email no estaba leído, lo actualizamos.
        if (!emailToRead.isRead) {
            emailToRead.isRead = true;
            this.unreadCount--; // Decrementamos el contador.
        }
        return emailToRead;
    }

    /**
     * Elimina todos los correos de la lista que ya han sido leídos.
     * Este es un algoritmo complejo porque modifica la lista mientras la recorre.
     *
     * @return El número de correos que fueron eliminados.
     */
    public int deleteReadEmails() {
        int deletedCount = 0;

        // Primero, manejamos el caso de que los primeros correos estén leídos.
        while (first != null && first.value.isRead) {
            first = first.next;
            deletedCount++;
        }

        // Si la lista no se quedó vacía, recorremos el resto.
        if (first != null) {
            Node previous = first;
            Node current = first.next;
            while (current != null) {
                if (current.value.isRead) {
                    // Correo leído, lo eliminamos haciendo el "bypass".
                    previous.next = current.next;
                    deletedCount++;
                    // 'previous' no se mueve, 'current' avanzará al nuevo 'previous.next'.
                } else {
                    // Correo no leído, lo dejamos. Avanzamos 'previous'.
                    previous = current;
                }
                current = previous.next;
            }
        }
        return deletedCount;
    }
    
    /**
     * Devuelve un array con todos los correos enviados por un remitente específico.
     *
     * @param sender El remitente por el que buscar.
     * @return Un array de objetos Email que coinciden con el remitente.
     */
    public Email[] searchBySender(String sender) {
        // Primer recorrido: Contar.
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.sender.equals(sender)) {
                count++;
            }
            current = current.next;
        }

        // Segundo recorrido: Crear y rellenar.
        Email[] emailsFromSender = new Email[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.sender.equals(sender)) {
                emailsFromSender[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return emailsFromSender;
    }
    
    /**
     * Elimina el correo en la posición 'index', lo considera spam y actualiza
     * el contador global de spam y el de no leídos si corresponde.
     *
     * @param index La posición del correo a eliminar.
     * @return El Email eliminado, o null si el índice es inválido.
     */
    public Email markAsSpamAndDrop(int index) {
        if (index < 0 || index >= getSize()) {
            return null;
        }

        Email spamEmail;
        // Lógica de eliminación (similar a playSong o removeStudent)
        if (index == 0) {
            spamEmail = first.value;
            first = first.next;
        } else {
            Node previous = first;
            for (int i = 0; i < index - 1; i++) {
                previous = previous.next;
            }
            Node nodeToRemove = previous.next;
            spamEmail = nodeToRemove.value;
            previous.next = nodeToRemove.next;
        }

        // Actualizar contadores
        if (!spamEmail.isRead) {
            this.unreadCount--; // Si no estaba leído, cuenta como uno menos.
        }
        Inbox.totalSpamDeleted++; // Incrementamos el contador global de spam.

        return spamEmail;
    }
}