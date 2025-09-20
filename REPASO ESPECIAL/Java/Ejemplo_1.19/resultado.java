/**
 * La clase GameLibrary gestiona una colección de videojuegos.
 * Hereda de LibraryBase para la funcionalidad básica de la lista.
 */
public class GameLibrary extends LibraryBase {

    // --- ATRIBUTOS ---
    
    private int totalHoursPlayedInLibrary = 0;
    // El atributo estático 'mostPlayedGenre' es complejo de mantener en tiempo real
    // sin estructuras de datos más avanzadas, por lo que se omite en esta implementación.

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Registra horas de juego para un videojuego específico.
     *
     * @param gameId El ID del juego.
     * @param hours  Las horas jugadas en esta sesión.
     */
    public void playGame(int gameId, int hours) {
        Node current = first;
        while (current != null) {
            VideoGame game = current.value;
            if (game.gameId == gameId) {
                game.hoursPlayed += hours;
                this.totalHoursPlayedInLibrary += hours;
                return;
            }
            current = current.next;
        }
    }

    /**
     * Encuentra y devuelve el juego con más horas jugadas.
     *
     * @return El objeto VideoGame más jugado, o null si la biblioteca está vacía.
     */
    public VideoGame getMostPlayedGame() {
        if (first == null) return null;

        VideoGame mostPlayed = first.value;
        Node current = first.next;
        while (current != null) {
            if (current.value.hoursPlayed > mostPlayed.hoursPlayed) {
                mostPlayed = current.value;
            }
            current = current.next;
        }
        return mostPlayed;
    }

    /**
     * Devuelve un array con todos los juegos de un género específico.
     *
     * @param genre El género a buscar.
     * @return Un array de objetos VideoGame.
     */
    public VideoGame[] getGamesByGenre(String genre) {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.genre.equals(genre)) count++;
            current = current.next;
        }

        VideoGame[] games = new VideoGame[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.genre.equals(genre)) {
                games[index++] = current.value;
            }
            current = current.next;
        }
        return games;
    }

    /**
     * Simula la venta o intercambio de un juego, eliminándolo de la biblioteca.
     *
     * @param gameId El ID del juego a intercambiar.
     * @return Las horas que se habían jugado a ese juego, o -1 si no se encontró.
     */
    public int tradeInGame(int gameId) {
        if (first == null) return -1;

        if (first.value.gameId == gameId) {
            int hours = first.value.hoursPlayed;
            this.totalHoursPlayedInLibrary -= hours;
            first = first.next;
            return hours;
        }

        Node prev = first;
        Node curr = first.next;
        while (curr != null) {
            if (curr.value.gameId == gameId) {
                int hours = curr.value.hoursPlayed;
                this.totalHoursPlayedInLibrary -= hours;
                prev.next = curr.next;
                return hours;
            }
            prev = curr;
            curr = curr.next;
        }
        return -1;
    }
}
