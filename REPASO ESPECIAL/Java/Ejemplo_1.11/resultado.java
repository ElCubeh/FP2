/**
 * La clase RestaurantQueue gestiona una cola de pedidos para un restaurante,
 * procesando los pedidos en el orden en que llegan.
 * Hereda de QueueBase para la funcionalidad básica de la lista.
 */
public class RestaurantQueue extends QueueBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena los ingresos totales de los pedidos servidos en ESTA cola.
     */
    private double totalRevenue = 0.0;

    /**
     * Contador estático para el total de pedidos servidos en TODOS los restaurantes.
     */
    private static int totalOrdersServed = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Sirve el primer pedido de la cola (el que lleva más tiempo esperando).
     * Lo elimina de la lista y actualiza los contadores de ingresos y pedidos.
     *
     * @return El objeto Order servido, o null si la cola está vacía.
     */
    public Order serveNextOrder() {
        if (first == null) {
            return null; // No hay pedidos en la cola.
        }

        // El pedido a servir es siempre el primero de la lista.
        Order orderServed = first.value;
        // Eliminamos el primer pedido moviendo el puntero 'first'.
        first = first.next;

        // Actualizamos los contadores.
        this.totalRevenue += orderServed.totalPrice;
        RestaurantQueue.totalOrdersServed++;

        return orderServed;
    }

    /**
     * Devuelve los ingresos totales acumulados en esta cola.
     *
     * @return El total de ingresos.
     */
    public double getCurrentRevenue() {
        return this.totalRevenue;
    }

    /**
     * Devuelve un array con todos los pedidos que están pendientes o cocinándose.
     *
     * @return Un array de objetos Order.
     */
    public Order[] getPendingOrders() {
        // Primer recorrido: Contar pedidos pendientes o cocinándose.
        int count = 0;
        Node current = first;
        while (current != null) {
            String status = current.value.status;
            if (status.equals("pending") || status.equals("cooking")) {
                count++;
            }
            current = current.next;
        }

        // Segundo recorrido: Crear y rellenar el array.
        Order[] pendingOrders = new Order[count];
        int index = 0;
        current = first;
        while (current != null) {
            String status = current.value.status;
            if (status.equals("pending") || status.equals("cooking")) {
                pendingOrders[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return pendingOrders;
    }

    /**
     * Cancela el pedido de una mesa específica si todavía está pendiente.
     *
     * @param tableNumber El número de la mesa cuyo pedido se quiere cancelar.
     * @return true si se canceló con éxito, false en caso contrario.
     */
    public boolean cancelOrder(int tableNumber) {
        if (first == null) {
            return false;
        }

        // Caso especial: el pedido a cancelar es el primero.
        if (first.value.tableNumber == tableNumber && first.value.status.equals("pending")) {
            first = first.next;
            return true;
        }

        // Caso general: el pedido está en el medio o al final.
        Node previous = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.tableNumber == tableNumber && current.value.status.equals("pending")) {
                previous.next = current.next; // Hacemos el bypass para eliminarlo.
                return true;
            }
            previous = current;
            current = current.next;
        }

        return false; // No se encontró un pedido cancelable para esa mesa.
    }
}
