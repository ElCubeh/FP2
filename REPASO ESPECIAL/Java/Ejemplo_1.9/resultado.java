/**
 * La clase PackageTracker gestiona el seguimiento de paquetes de mensajería.
 * Hereda de TrackerBase, que ya proporciona la búsqueda de paquetes.
 * Añade métodos para actualizar estados y gestionar paquetes entregados.
 */
public class PackageTracker extends TrackerBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el número de paquetes marcados como "Delivered" en ESTE tracker.
     */
    private int deliveredCount = 0;

    /**
     * Almacena el número total de paquetes enviados en TODOS los trackers.
     * Es 'static' para ser un contador global compartido.
     */
    private static int totalPackagesShipped = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Actualiza el estado de un paquete, buscándolo por su número de seguimiento.
     *
     * @param trackingNumber El número de seguimiento del paquete a actualizar.
     * @param newStatus      El nuevo estado a asignar.
     * @return true si el paquete fue encontrado y actualizado, false en caso contrario.
     */
    public boolean updateStatus(String trackingNumber, String newStatus) {
        // Usamos el método heredado findPackage() para buscar el paquete.
        Package packageFound = findPackage(trackingNumber);

        if (packageFound != null) { // Si lo encontró...
            // Solo incrementamos el contador si es la PRIMERA vez que se marca como entregado.
            if (!packageFound.status.equals("Delivered") && newStatus.equals("Delivered")) {
                this.deliveredCount++;
            }
            // Actualizamos el estado.
            packageFound.status = newStatus;
            return true;
        } else {
            // Si findPackage() devolvió null, no lo encontró.
            return false;
        }
    }

    /**
     * Devuelve un array con todos los paquetes que ya han sido entregados.
     *
     * @return Un array de Package cuyo estado es "Delivered".
     */
    public Package[] getDeliveredPackages() {
        // Primer recorrido: Contar cuántos paquetes están entregados.
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.status.equals("Delivered")) {
                count++;
            }
            current = current.next;
        }

        // Segundo recorrido: Crear el array del tamaño exacto y rellenarlo.
        Package[] deliveredPackages = new Package[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.status.equals("Delivered")) {
                deliveredPackages[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return deliveredPackages;
    }

    /**
     * Cuenta el número de paquetes que se dirigen a un destino específico.
     *
     * @param destination El destino a buscar.
     * @return El número de paquetes que van a ese destino.
     */
    public int countPackagesByDestination(String destination) {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.destination.equals(destination)) {
                count++;
            }
            current = current.next;
        }
        return count;
    }

    /**
     * Elimina de la lista todos los paquetes que ya han sido entregados.
     */
    public void removeDelivered() {
        // Caso especial: eliminar desde el principio de la lista.
        while (first != null && first.value.status.equals("Delivered")) {
            first = first.next;
        }

        // Si la lista no se ha quedado vacía, recorremos el resto.
        if (first != null) {
            Node previous = first;
            Node current = first.next;
            while (current != null) {
                if (current.value.status.equals("Delivered")) {
                    // Eliminamos el nodo 'current' haciendo el bypass.
                    previous.next = current.next;
                } else {
                    // Si no lo eliminamos, 'previous' avanza.
                    previous = current;
                }
                current = previous.next;
            }
        }
    }
}
