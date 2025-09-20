/**
 * La clase ShoppingCart simula un carrito de la compra de un e-commerce.
 * Hereda de CartBase para la funcionalidad básica de la lista.
 */
public class ShoppingCart extends CartBase {

    // --- ATRIBUTOS ---
    // Esta clase no necesita atributos propios.

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Actualiza la cantidad de un artículo en el carrito.
     * Si la nueva cantidad es 0, el artículo se elimina.
     *
     * @param productId     El ID del producto a actualizar.
     * @param newQuantity   La nueva cantidad.
     * @return true si la operación tuvo éxito, false en caso contrario.
     */
    public boolean updateItemQuantity(String productId, int newQuantity) {
        if (first == null) return false;

        // Si la cantidad es 0, tratamos de eliminarlo.
        if (newQuantity <= 0) {
            // Caso especial: eliminar el primer artículo.
            if (first.value.productId.equals(productId)) {
                first = first.next;
                return true;
            }
            // Caso general: eliminar del resto.
            Node previous = first;
            Node current = first.next;
            while (current != null) {
                if (current.value.productId.equals(productId)) {
                    previous.next = current.next;
                    return true;
                }
                previous = current;
                current = current.next;
            }
            return false; // No se encontró para eliminar.
        } else {
            // Si la cantidad es > 0, tratamos de actualizarlo.
            Node current = first;
            while (current != null) {
                if (current.value.productId.equals(productId)) {
                    current.value.quantity = newQuantity;
                    return true;
                }
                current = current.next;
            }
            return false; // No se encontró para actualizar.
        }
    }

    /**
     * Calcula el precio total de todos los artículos en el carrito.
     *
     * @return El precio total como un double.
     */
    public double getTotalPrice() {
        double totalPrice = 0.0;
        Node current = first;
        while (current != null) {
            CartItem item = current.value;
            totalPrice += item.price * item.quantity;
            current = current.next;
        }
        return totalPrice;
    }

    /**
     * Devuelve el número total de artículos (sumando cantidades).
     *
     * @return El número total de artículos.
     */
    public int getItemCount() {
        int totalItems = 0;
        Node current = first;
        while (current != null) {
            totalItems += current.value.quantity;
            current = current.next;
        }
        return totalItems;
    }

    /**
     * Vacía completamente el carrito de la compra.
     */
    public void emptyCart() {
        first = null;
    }
}
