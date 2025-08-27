/**
 * La clase Inventory gestiona el inventario de productos de una tienda.
 * Hereda de InventoryBase para reutilizar la estructura de la lista enlazada.
 * Añade funcionalidades para vender, reponer, y analizar el inventario.
 */
public class Inventory extends InventoryBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena los ingresos totales generados por las ventas en ESTA instancia
     * de inventario. Es una variable de instancia, cada objeto Inventory
     * tendrá su propia copia.
     */
    private double totalRevenue = 0.0;

    /**
     * Almacena el número total de unidades de producto vendidas en TODAS
     * las instancias de Inventory. Es 'static', lo que significa que es una
     * variable compartida por todos los objetos de esta clase.
     */
    private static int totalProductsSold = 0;


    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Vende una cantidad específica de un producto, buscándolo por su ID.
     *
     * @param productId El ID del producto a vender.
     * @param quantity  La cantidad de unidades a vender.
     * @return El valor total de la venta (precio * cantidad) si fue exitosa,
     * o 0.0 si el producto no se encontró o no había stock suficiente.
     */
    public double sellProduct(int productId, int quantity) {
        // Empezamos el recorrido desde el primer nodo de la lista.
        Node current = first;

        // Recorremos la lista mientras no lleguemos al final (current != null).
        while (current != null) {
            Product product = current.value; // Obtenemos el producto del nodo actual.

            // Comprobamos si el ID del producto actual coincide con el que buscamos.
            if (product.productId == productId) {
                // ¡Producto encontrado! Ahora verificamos si hay stock suficiente.
                if (product.quantity >= quantity) {
                    // Hay stock. Procedemos con la venta.
                    product.quantity -= quantity; // 1. Reducimos el stock del producto.

                    double saleValue = product.price * quantity; // 2. Calculamos el valor de la venta.

                    this.totalRevenue += saleValue; // 3. Sumamos al ingreso de esta tienda.
                    Inventory.totalProductsSold += quantity; // 4. Sumamos al contador global de ventas.

                    return saleValue; // 5. Devolvemos el valor de la venta y terminamos.
                } else {
                    // No hay suficiente stock, la venta no es posible.
                    return 0.0;
                }
            }
            // Si no es el producto que buscamos, avanzamos al siguiente nodo.
            current = current.next;
        }

        // Si el bucle termina, significa que el producto no estaba en la lista.
        return 0.0;
    }

    /**
     * Calcula el valor monetario total de todo el inventario.
     * (Suma de la cantidad * precio de cada producto).
     *
     * @return El valor total del inventario como un double.
     */
    public double getTotalInventoryValue() {
        double totalValue = 0.0;
        Node current = first; // Empezamos el recorrido.

        while (current != null) {
            Product product = current.value;
            // Sumamos el valor del stock de este producto al total.
            totalValue += product.quantity * product.price;
            current = current.next; // Avanzamos al siguiente.
        }
        return totalValue;
    }

    /**
     * Aumenta el stock de un producto existente, buscándolo por su ID.
     *
     * @param productId El ID del producto a reponer.
     * @param quantity  La cantidad de unidades a añadir al stock.
     * @return true si el producto fue encontrado y actualizado, false en caso contrario.
     */
    public boolean restockProduct(int productId, int quantity) {
        Node current = first; // Empezamos el recorrido.

        while (current != null) {
            Product product = current.value;
            if (product.productId == productId) {
                // ¡Producto encontrado!
                product.quantity += quantity; // Aumentamos su stock.
                return true; // Indicamos que la operación fue exitosa.
            }
            current = current.next;
        }

        // Si el bucle termina, el producto no se encontró.
        return false;
    }

    /**
     * Devuelve un array con todos los productos cuyo stock está por debajo de un umbral.
     *
     * @param threshold El límite de stock.
     * @return Un array de objetos Product que cumplen la condición.
     */
    public Product[] getProductsBelowStock(int threshold) {
        // --- Primer recorrido: Contar para saber el tamaño del array ---
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.quantity < threshold) {
                count++;
            }
            current = current.next;
        }

        // --- Segundo recorrido: Crear el array y rellenarlo ---
        Product[] lowStockProducts = new Product[count]; // Creamos el array del tamaño exacto.
        int index = 0;
        current = first; // Reiniciamos el recorrido.
        while (current != null) {
            if (current.value.quantity < threshold) {
                lowStockProducts[index] = current.value; // Añadimos el producto al array.
                index++; // Preparamos el índice para el siguiente.
            }
            current = current.next;
        }

        return lowStockProducts;
    }
}
