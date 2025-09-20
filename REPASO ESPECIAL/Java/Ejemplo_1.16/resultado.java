/**
 * La clase RealEstateAgency gestiona listados de propiedades inmobiliarias.
 * Hereda de AgencyBase para la funcionalidad básica de la lista.
 */
public class RealEstateAgency extends AgencyBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena las comisiones ganadas por ESTA agencia.
     */
    private double commissionEarned = 0.0;

    /**
     * Contador estático del total de propiedades vendidas por TODAS las agencias.
     */
    private static int totalPropertiesSold = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Marca una propiedad como vendida y calcula la comisión.
     *
     * @param address         La dirección de la propiedad vendida.
     * @param commissionRate  La tasa de comisión (ej. 0.05 para un 5%).
     * @return El precio de venta de la propiedad, o 0 si no se pudo vender.
     */
    public double sellProperty(String address, double commissionRate) {
        Node current = first;
        while (current != null) {
            Property prop = current.value;
            if (prop.address.equals(address) && prop.isAvailable) {
                prop.isAvailable = false;
                this.commissionEarned += prop.price * commissionRate;
                RealEstateAgency.totalPropertiesSold++;
                return prop.price;
            }
            current = current.next;
        }
        return 0.0; // No se encontró la propiedad o no estaba disponible.
    }

    /**
     * Devuelve un array con todas las propiedades disponibles.
     *
     * @return Un array de objetos Property.
     */
    public Property[] getAvailableProperties() {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.isAvailable) count++;
            current = current.next;
        }

        Property[] available = new Property[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.isAvailable) {
                available[index++] = current.value;
            }
            current = current.next;
        }
        return available;
    }

    /**
     * Devuelve un array de propiedades disponibles por debajo de un precio máximo.
     *
     * @param maxPrice El precio máximo.
     * @return Un array de objetos Property.
     */
    public Property[] getPropertiesBelowPrice(double maxPrice) {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.isAvailable && current.value.price < maxPrice) {
                count++;
            }
            current = current.next;
        }

        Property[] affordable = new Property[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.isAvailable && current.value.price < maxPrice) {
                affordable[index++] = current.value;
            }
            current = current.next;
        }
        return affordable;
    }

    /**
     * Calcula el precio medio por metro cuadrado de las propiedades disponibles.
     *
     * @return El precio medio por m2.
     */
    public double calculateAveragePricePerSquareMeter() {
        double totalPrice = 0.0;
        int totalMeters = 0;
        Node current = first;
        while (current != null) {
            if (current.value.isAvailable) {
                totalPrice += current.value.price;
                totalMeters += current.value.squareMeters;
            }
            current = current.next;
        }

        if (totalMeters == 0) {
            return 0.0; // Evitar división por cero.
        }
        return totalPrice / totalMeters;
    }
}
