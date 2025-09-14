/**
 * La clase VotingSystem gestiona un sistema de votación electoral.
 * Hereda de VotingSystemBase para la funcionalidad básica de la lista enlazada.
 * Añade métodos para contar votos, determinar un ganador y anular votos.
 */
public class VotingSystem extends VotingSystemBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el número de votos que han sido anulados en ESTE sistema de votación.
     */
    private int invalidatedVotes = 0;

    /**
     * Almacena el número total de votos válidos emitidos en TODOS los sistemas.
     * Es 'static' para ser un contador global y 'long' para admitir grandes números.
     */
    private static long totalValidVotesCast = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Cuenta y devuelve el número total de votos para un candidato específico.
     * @param candidateName El nombre del candidato a buscar.
     * @return El número de votos para ese candidato.
     */
    public int countVotesFor(String candidateName) {
        int voteCount = 0;
        Node current = first;
        while (current != null) {
            Vote vote = current.value;
            if (vote.candidateName.equals(candidateName)) {
                voteCount++;
            }
            current = current.next;
        }
        return voteCount;
    }

    /**
     * Determina el ganador de la elección basándose en el recuento de votos.
     * No es muy eficiente, ya que recalcula los votos para cada candidato.
     * @return El nombre del candidato ganador, o "Tie" si hay un empate.
     */
    public String getWinner() {
        String winnerName = null;
        int maxVotes = -1;
        Node current = first;

        while (current != null) {
            String currentCandidateName = current.value.candidateName;
            int voteCount = countVotesFor(currentCandidateName);

            if (voteCount > maxVotes) {
                // Nuevo ganador claro
                maxVotes = voteCount;
                winnerName = currentCandidateName;
            } else if (voteCount == maxVotes) {
                // Posible empate
                if (winnerName != null && !winnerName.equals(currentCandidateName)) {
                    winnerName = "Tie";
                }
            }
            current = current.next;
        }
        return winnerName;
    }

    /**
     * Elimina todos los votos emitidos por un votante específico (voterId).
     * @param voterId El ID del votante cuyos votos serán anulados.
     * @return El número de votos que fueron eliminados.
     */
    public int invalidateVotes(int voterId) {
        int deletedCount = 0;

        // Caso especial: eliminar desde el principio de la lista.
        while (first != null && first.value.voterId == voterId) {
            first = first.next;
            deletedCount++;
        }

        // Caso general: eliminar del resto de la lista.
        if (first != null) {
            Node previous = first;
            Node current = first.next;
            while (current != null) {
                if (current.value.voterId == voterId) {
                    previous.next = current.next;
                    deletedCount++;
                } else {
                    previous = current;
                }
                current = previous.next;
            }
        }

        // Actualiza el contador de la clase y devuelve el recuento de esta operación.
        this.invalidatedVotes += deletedCount;
        return deletedCount;
    }

    /**
     * Devuelve una lista de todos los votantes únicos que han participado.
     * @return Un array de int con los voterId sin duplicados.
     */
    public int[] getVotersList() {
        // Array temporal sobredimensionado.
        int[] tempVoters = new int[getSize()];
        int uniqueVotersCount = 0;
        Node current = first;

        while (current != null) {
            int currentVoterId = current.value.voterId;
            boolean isDuplicate = false;
            // Bucle anidado para buscar duplicados.
            for (int i = 0; i < uniqueVotersCount; i++) {
                if (tempVoters[i] == currentVoterId) {
                    isDuplicate = true;
                    break;
                }
            }
            // Si no es un duplicado, lo añadimos.
            if (!isDuplicate) {
                tempVoters[uniqueVotersCount] = currentVoterId;
                uniqueVotersCount++;
            }
            current = current.next;
        }

        // Copiamos a un array final del tamaño exacto.
        int[] finalVotersList = new int[uniqueVotersCount];
        for (int i = 0; i < uniqueVotersCount; i++) {
            finalVotersList[i] = tempVoters[i];
        }
        return finalVotersList;
    }
}