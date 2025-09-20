/**
 * La clase CarFleet gestiona una flota de coches de alquiler.
 * Hereda de FleetBase para la funcionalidad básica de la lista.
 */
public class CarFleet extends FleetBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el número de coches actualmente alquilados en ESTA flota.
     */
    private int rentedCarsCount = 0;

    /**
     * Contador estático para el total de kilómetros recorridos por TODOS los coches.
     */
    private static long totalKilometersDriven = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Alquila un coche si está disponible.
     *
     * @param licensePlate La matrícula del coche a alquilar.
     * @return El objeto RentalCar alquilado, o null si no fue posible.
     */
    public RentalCar rentCar(String licensePlate) {
        Node current = first;
        while (current != null) {
            RentalCar car = current.value;
            if (car.licensePlate.equals(licensePlate)) {
                if (!car.isRented) {
                    car.isRented = true;
                    this.rentedCarsCount++;
                    return car;
                } else {
                    return null; // El coche ya estaba alquilado.
                }
            }
            current = current.next;
        }
        return null; // No se encontró el coche.
    }

    /**
     * Gestiona la devolución de un coche.
     *
     * @param licensePlate       La matrícula del coche devuelto.
     * @param kilometersDriven   Los kilómetros recorridos durante el alquiler.
     */
    public void returnCar(String licensePlate, int kilometersDriven) {
        Node current = first;
        while (current != null) {
            RentalCar car = current.value;
            if (car.licensePlate.equals(licensePlate)) {
                if (car.isRented) {
                    car.isRented = false;
                    car.mileage += kilometersDriven;
                    this.rentedCarsCount--;
                    CarFleet.totalKilometersDriven += kilometersDriven;
                }
                return; // Salimos del método una vez encontrado el coche.
            }
            current = current.next;
        }
    }

    /**
     * Devuelve un array con todos los coches disponibles para alquilar.
     *
     * @return Un array de objetos RentalCar.
     */
    public RentalCar[] getAvailableCars() {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (!current.value.isRented) {
                count++;
            }
            current = current.next;
        }

        RentalCar[] availableCars = new RentalCar[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (!current.value.isRented) {
                availableCars[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return availableCars;
    }

    /**
     * Encuentra y devuelve el coche con el mayor kilometraje de la flota.
     *
     * @return El RentalCar con más kilómetros, o null si la flota está vacía.
     */
    public RentalCar getCarWithHighestMileage() {
        if (first == null) {
            return null;
        }

        RentalCar carWithMaxMileage = first.value;
        Node current = first.next;
        while (current != null) {
            if (current.value.mileage > carWithMaxMileage.mileage) {
                carWithMaxMileage = current.value;
            }
            current = current.next;
        }
        return carWithMaxMileage;
    }
}