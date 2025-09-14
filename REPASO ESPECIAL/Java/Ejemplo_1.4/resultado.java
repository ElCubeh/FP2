/**
 * La clase StudentRegistry gestiona una lista de estudiantes en un curso.
 * Hereda de RegistryBase para la funcionalidad básica de la lista.
 * Añade métodos para asignar calificaciones, calcular promedios, y más.
 */
public class StudentRegistry extends RegistryBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena el número de estudiantes en ESTE registro que ya tienen una
     * calificación asignada (diferente de -1.0).
     */
    private int gradedStudentsCount = 0;

    /**
     * Almacena la calificación más alta registrada en CUALQUIER instancia
     * de StudentRegistry. Es 'static', por lo que es compartida globalmente.
     */
    private static double highestGradeEver = 0.0;


    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Asigna una calificación a un estudiante, buscándolo por su ID.
     * Actualiza los contadores de estudiantes calificados y la nota más alta.
     *
     * @param studentId El ID del estudiante a calificar.
     * @param grade     La calificación a asignar.
     * @return true si el estudiante fue encontrado y calificado, false si no.
     */
    public boolean assignGrade(String studentId, double grade) {
        Node current = first;
        while (current != null) {
            Student student = current.value;
            if (student.studentId.equals(studentId)) {
                // Estudiante encontrado.
                // Si era la primera vez que lo calificábamos (nota era -1.0), incrementamos el contador.
                if (student.grade == -1.0) {
                    this.gradedStudentsCount++;
                }
                // Asignamos la nueva calificación.
                student.grade = grade;
                // Si esta nota es la más alta de todas, la guardamos en la variable estática.
                if (grade > StudentRegistry.highestGradeEver) {
                    StudentRegistry.highestGradeEver = grade;
                }
                return true; // Operación exitosa.
            }
            current = current.next;
        }
        // Si el bucle termina, el estudiante no fue encontrado.
        return false;
    }

    /**
     * Calcula la calificación promedio de los estudiantes que ya han sido calificados.
     *
     * @return El promedio como un double, o 0.0 si no hay estudiantes calificados.
     */
    public double calculateAverageGrade() {
        double totalGrades = 0.0;
        int studentsCounted = 0;
        Node current = first;

        // Recorremos la lista para sumar notas y contar estudiantes calificados.
        while (current != null) {
            Student student = current.value;
            if (student.grade != -1.0) {
                totalGrades += student.grade;
                studentsCounted++;
            }
            current = current.next;
        }

        // Para evitar división por cero, comprobamos si contamos algún estudiante.
        if (studentsCounted == 0) {
            return 0.0;
        } else {
            return totalGrades / studentsCounted;
        }
    }

    /**
     * Elimina a un estudiante de la lista, buscándolo por su ID.
     *
     * @param studentId El ID del estudiante a eliminar.
     * @return El objeto Student eliminado, o null si no se encontró.
     */
    public Student removeStudent(String studentId) {
        if (first == null) return null;

        // Caso especial: el estudiante a eliminar es el primero.
        if (first.value.studentId.equals(studentId)) {
            Student studentRemoved = first.value;
            first = first.next;
            return studentRemoved;
        }

        // Caso general: está en el medio o al final.
        Node previous = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.studentId.equals(studentId)) {
                previous.next = current.next; // Hacemos el "bypass".
                return current.value;
            }
            previous = current;
            current = current.next;
        }

        // No se encontró al estudiante.
        return null;
    }

    /**
     * Devuelve un array con todos los estudiantes que aún no han sido calificados.
     *
     * @return Un array de objetos Student cuya calificación es -1.0.
     */
    public Student[] getStudentsWithoutGrade() {
        // Primer recorrido: Contar para saber el tamaño del array.
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.grade == -1.0) {
                count++;
            }
            current = current.next;
        }

        // Segundo recorrido: Crear el array y rellenarlo.
        Student[] studentsWithoutGrade = new Student[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.grade == -1.0) {
                studentsWithoutGrade[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return studentsWithoutGrade;
    }
}