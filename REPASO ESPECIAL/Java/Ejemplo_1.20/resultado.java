/**
 * La clase HotelBookings gestiona las reservas de un hotel.
 * Hereda de BookingsBase para la funcionalidad básica de la lista.
 */
public class HotelBookings extends BookingsBase {

    // --- ATRIBUTOS ---

    private int occupiedRoomsCount = 0;
    private static int totalNightsBooked = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Simula el check-in de un huésped basado en su ID de reserva.
     *
     * @param bookingId El ID de la reserva.
     * @return El número de noches de la reserva, o -1 si no se encontró.
     */
    public int checkIn(int bookingId) {
        Node current = first;
        while (current != null) {
            Booking booking = current.value;
            if (booking.bookingId == bookingId) {
                this.occupiedRoomsCount++;
                HotelBookings.totalNightsBooked += booking.nights;
                return booking.nights;
            }
            current = current.next;
        }
        return -1;
    }

    /**
     * Simula el check-out de un huésped, eliminando su reserva por número de habitación.
     *
     * @param roomNumber El número de la habitación que se desocupa.
     * @return La reserva finalizada, o null si no había ninguna para esa habitación.
     */
    public Booking checkOut(int roomNumber) {
        if (first == null) return null;
        Booking checkedOutBooking;
        if (first.value.roomNumber == roomNumber) {
            checkedOutBooking = first.value;
            first = first.next;
        } else {
            Node prev = first;
            Node curr = first.next;
            while (curr != null) {
                if (curr.value.roomNumber == roomNumber) {
                    checkedOutBooking = curr.value;
                    prev.next = curr.next;
                    this.occupiedRoomsCount--;
                    return checkedOutBooking;
                }
                prev = curr;
                curr = curr.next;
            }
            return null;
        }
        this.occupiedRoomsCount--;
        return checkedOutBooking;
    }

    /**
     * Encuentra la primera reserva asociada a un nombre de huésped.
     *
     * @param guestName El nombre del huésped a buscar.
     * @return El objeto Booking, o null si no se encontró.
     */
    public Booking findBookingByGuest(String guestName) {
        Node current = first;
        while (current != null) {
            if (current.value.guestName.equals(guestName)) {
                return current.value;
            }
            current = current.next;
        }
        return null;
    }

    /**
     * Devuelve un array con los números de todas las habitaciones ocupadas.
     * Para esta implementación, asumimos que todas las reservas en la lista
     * corresponden a habitaciones actualmente ocupadas.
     *
     * @return Un array de int con los números de habitación.
     */
    public int[] getRoomsOccupied() {
        int count = getSize(); // Usamos un método de la clase base.
        int[] occupiedRooms = new int[count];
        int index = 0;
        Node current = first;
        while (current != null) {
            occupiedRooms[index++] = current.value.roomNumber;
            current = current.next;
        }
        return occupiedRooms;
    }
}