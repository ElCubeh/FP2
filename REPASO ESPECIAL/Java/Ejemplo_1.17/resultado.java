/**
 * La clase GymRegister gestiona a los miembros de un gimnasio.
 * Hereda de RegisterBase para la funcionalidad básica de la lista.
 */
public class GymRegister extends RegisterBase {

    // --- ATRIBUTOS ---

    private int premiumMembersCount = 0;
    private static long totalCheckIns = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Registra la visita de un miembro.
     *
     * @param memberId El ID del miembro.
     * @return El nuevo número total de visitas de ese miembro, o -1 si no se encontró.
     */
    public int checkInMember(int memberId) {
        Node current = first;
        while (current != null) {
            Member member = current.value;
            if (member.memberId == memberId) {
                member.visits++;
                GymRegister.totalCheckIns++;
                return member.visits;
            }
            current = current.next;
        }
        return -1;
    }

    /**
     * Mejora la membresía de un miembro a "Premium".
     *
     * @param memberId El ID del miembro a mejorar.
     */
    public void upgradeToPremium(int memberId) {
        Node current = first;
        while (current != null) {
            Member member = current.value;
            if (member.memberId == memberId) {
                if (!member.membershipType.equals("Premium")) {
                    member.membershipType = "Premium";
                    this.premiumMembersCount++;
                }
                return;
            }
            current = current.next;
        }
    }

    /**
     * Encuentra al miembro con más visitas.
     *
     * @return El objeto Member más activo, o null si el registro está vacío.
     */
    public Member getMostActiveMember() {
        if (first == null) return null;
        Member mostActive = first.value;
        Node current = first.next;
        while (current != null) {
            if (current.value.visits > mostActive.visits) {
                mostActive = current.value;
            }
            current = current.next;
        }
        return mostActive;
    }

    /**
     * Elimina a todos los miembros con menos visitas que un umbral mínimo.
     *
     * @param minVisits El número mínimo de visitas para no ser eliminado.
     * @return El número de miembros eliminados.
     */
    public int removeInactiveMembers(int minVisits) {
        int removedCount = 0;
        // Eliminar desde el principio.
        while (first != null && first.value.visits < minVisits) {
            first = first.next;
            removedCount++;
        }

        if (first == null) return removedCount;

        // Eliminar del resto de la lista.
        Node previous = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.visits < minVisits) {
                previous.next = current.next;
                removedCount++;
            } else {
                previous = current;
            }
            current = previous.next;
        }
        return removedCount;
    }
}
