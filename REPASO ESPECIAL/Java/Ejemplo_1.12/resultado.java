/**
 * La clase PatientList gestiona una lista de pacientes en un hospital.
 * Hereda de PatientListBase para la funcionalidad básica de la lista.
 */
public class PatientList extends PatientListBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el número de pacientes con prioridad "Urgente" en ESTA lista.
     */
    private int urgentPatientsCount = 0;

    /**
     * Contador estático para el total de pacientes dados de alta en TODOS los hospitales.
     */
    private static int totalPatientsDischarged = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Da de alta a un paciente, eliminándolo de la lista.
     *
     * @param patientId El ID del paciente a dar de alta.
     * @return El objeto Patient dado de alta, o null si no se encontró.
     */
    public Patient dischargePatient(String patientId) {
        if (first == null) return null;

        Patient patientDischarged;

        // Caso especial: el paciente a dar de alta es el primero.
        if (first.value.patientId.equals(patientId)) {
            patientDischarged = first.value;
            first = first.next;
        } else {
            // Caso general: buscar en el resto de la lista.
            Node previous = first;
            Node current = first.next;
            while (current != null) {
                if (current.value.patientId.equals(patientId)) {
                    patientDischarged = current.value;
                    previous.next = current.next; // Eliminar el nodo.

                    // Actualizar contadores si se encontró y eliminó.
                    if (patientDischarged.priority == 1) {
                        this.urgentPatientsCount--;
                    }
                    PatientList.totalPatientsDischarged++;
                    return patientDischarged;
                }
                previous = current;
                current = current.next;
            }
            return null; // No se encontró al paciente.
        }

        // Actualizar contadores si se eliminó el primer paciente.
        if (patientDischarged.priority == 1) {
            this.urgentPatientsCount--;
        }
        PatientList.totalPatientsDischarged++;
        return patientDischarged;
    }

    /**
     * Devuelve un array con todos los pacientes urgentes (prioridad 1).
     *
     * @return Un array de objetos Patient.
     */
    public Patient[] getUrgentPatients() {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.priority == 1) {
                count++;
            }
            current = current.next;
        }

        Patient[] urgentPatients = new Patient[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.priority == 1) {
                urgentPatients[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return urgentPatients;
    }

    /**
     * Actualiza el diagnóstico de un paciente específico.
     *
     * @param patientId      El ID del paciente.
     * @param newDiagnosis   El nuevo diagnóstico.
     * @return true si se actualizó con éxito, false en caso contrario.
     */
    public boolean updateDiagnosis(String patientId, String newDiagnosis) {
        Node current = first;
        while (current != null) {
            if (current.value.patientId.equals(patientId)) {
                current.value.diagnosis = newDiagnosis;
                return true;
            }
            current = current.next;
        }
        return false;
    }

    /**
     * Encuentra y devuelve el primer paciente urgente en la lista sin eliminarlo.
     *
     * @return El primer Patient con prioridad 1, o null si no hay ninguno.
     */
    public Patient findNextUrgentPatient() {
        Node current = first;
        while (current != null) {
            if (current.value.priority == 1) {
                return current.value;
            }
            current = current.next;
        }
        return null;
    }
}
