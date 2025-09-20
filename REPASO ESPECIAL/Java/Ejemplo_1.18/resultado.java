/**
 * La clase CourseRoster gestiona las inscripciones de estudiantes en un curso.
 * Hereda de RosterBase para la funcionalidad básica de la lista.
 */
public class CourseRoster extends RosterBase {

    // --- ATRIBUTOS ---

    private int passCount = 0;
    private static double highestGradeInUniversity = 0.0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Asigna una calificación a un estudiante.
     *
     * @param studentId El ID del estudiante.
     * @param grade     La calificación a asignar.
     */
    public void assignGrade(String studentId, double grade) {
        Node current = first;
        while (current != null) {
            Enrollment enrollment = current.value;
            if (enrollment.studentId.equals(studentId)) {
                // Si el estudiante ya estaba aprobado y se le cambia la nota, ajustamos.
                if (enrollment.grade >= 5.0) {
                    this.passCount--;
                }
                enrollment.grade = grade;
                if (enrollment.grade >= 5.0) {
                    this.passCount++;
                }
                if (grade > CourseRoster.highestGradeInUniversity) {
                    CourseRoster.highestGradeInUniversity = grade;
                }
                return;
            }
            current = current.next;
        }
    }

    /**
     * Calcula el porcentaje de aprobados sobre los estudiantes calificados.
     *
     * @return El porcentaje de aprobados (0.0 a 100.0).
     */
    public double calculatePassRate() {
        int qualifiedCount = 0;
        Node current = first;
        while (current != null) {
            if (current.value.grade != -1.0) {
                qualifiedCount++;
            }
            current = current.next;
        }

        if (qualifiedCount == 0) return 0.0;
        return ((double) this.passCount / qualifiedCount) * 100.0;
    }

    /**
     * Devuelve un array con las inscripciones de los estudiantes suspensos.
     *
     * @return Un array de objetos Enrollment.
     */
    public Enrollment[] getFailingStudents() {
        int count = 0;
        Node current = first;
        while (current != null) {
            double grade = current.value.grade;
            if (grade >= 0.0 && grade < 5.0) count++;
            current = current.next;
        }

        Enrollment[] failing = new Enrollment[count];
        int index = 0;
        current = first;
        while (current != null) {
            double grade = current.value.grade;
            if (grade >= 0.0 && grade < 5.0) {
                failing[index++] = current.value;
            }
            current = current.next;
        }
        return failing;
    }

    /**
     * Da de baja a un estudiante del curso.
     *
     * @param studentId El ID del estudiante a dar de baja.
     * @return La inscripción eliminada, o null si no se encontró.
     */
    public Enrollment dropStudent(String studentId) {
        if (first == null) return null;
        Enrollment dropped;
        if (first.value.studentId.equals(studentId)) {
            dropped = first.value;
            first = first.next;
        } else {
            Node prev = first;
            Node curr = first.next;
            while (curr != null) {
                if (curr.value.studentId.equals(studentId)) {
                    dropped = curr.value;
                    prev.next = curr.next;
                    if (dropped.grade >= 5.0) this.passCount--;
                    return dropped;
                }
                prev = curr;
                curr = curr.next;
            }
            return null;
        }
        if (dropped.grade >= 5.0) this.passCount--;
        return dropped;
    }
}
