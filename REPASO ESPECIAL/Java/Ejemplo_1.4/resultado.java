public class StudentRegistry extends RegistryBase{
    private int gradedStudentsCount = 0;
    private static double highestGradeEver = 0;
    public boolean assignGrade(String studentId, double grade) {
    Node current = first; // Empezamos el recorrido.

    while (current != null) {
        // 1. Obtenemos el objeto Student del nodo actual.
        Student student = current.value;

        // 2. Comparamos el studentId del estudiante actual con el que buscamos.
        if (student.studentId.equals(studentId)) {
            // ¡Estudiante encontrado!

            // 3. Comprobamos si era la primera vez que lo calificábamos.
            if (student.grade == -1.0) {
                this.gradedStudentsCount++; // Si es así, incrementamos el contador.
            }

            // 4. Asignamos la nueva calificación.
            student.grade = grade;

            // 5. Comprobamos si esta nueva nota es la más alta registrada.
            if (grade > StudentRegistry.highestGradeEver) {
                StudentRegistry.highestGradeEver = grade;
            }

            // 6. Devolvemos true porque la operación fue exitosa.
            return true;
        }

        // 7. ¡Muy importante! Avanzamos al siguiente nodo.
        current = current.next;
    }

    // 8. Si el bucle termina, el estudiante no fue encontrado.
    return false;
}
    public double calculateAverageGrade() {
        double totalGrades = 0.0;
        int studentsCounted = 0;
        Node current = first; // 1. Empezamos desde el principio.

        // --- Primer paso: Recorrer la lista para sumar y contar ---
        while (current != null) {
            // 2. Obtenemos el estudiante de este nodo.
            Student student = current.value;

            if (student.grade != -1.0) { // Si el estudiante está calificado...
                // 3. Sumamos su nota al total.
                totalGrades += student.grade;
                // Y lo contamos.
                studentsCounted++;
            }
            current = current.next; // Avanzamos al siguiente.
        }

        // --- Segundo paso: Calcular el promedio DESPUÉS del bucle ---
        // 5. Comprobamos si encontramos algún estudiante calificado.
        if (studentsCounted == 0) {
            // Si no, devolvemos 0.0 para evitar la división por cero.
            return 0.0;
        } else {
            // Si sí, calculamos el promedio y lo devolvemos.
            // 6. Añadimos el return.
            return totalGrades / studentsCounted;
        }
    }
    public Student removeStudent(String studentId) {
        // Si la lista está vacía, no hay nada que hacer.
        if (first == null) {
            return null;
        }

        // --- CASO ESPECIAL: El estudiante a eliminar es el primero ---
        if (first.value.studentId.equals(studentId)) {
            Student studentRemoved = first.value; // Guardamos el estudiante.
            first = first.next;                   // Lo desenganchamos moviendo el puntero 'first'.
            return studentRemoved;                // Lo devolvemos.
        }

        // --- CASO GENERAL: El estudiante está en el medio o al final ---
        Node previous = first;
        Node current = first.next;

        // Recorremos el resto de la lista.
        while (current != null) {
            // Comprobamos si el nodo 'current' es el que buscamos.
            if (current.value.studentId.equals(studentId)) {
                // ¡Lo encontramos!
                // Hacemos que el nodo anterior se salte al actual.
                previous.next = current.next;
                // Devolvemos el estudiante del nodo que acabamos de desenganchar.
                return current.value;
            }
            // Si no es este, avanzamos los dos punteros.
            previous = current;
            current = current.next;
        }

        // Si el bucle termina, significa que no encontramos al estudiante.
        return null;
    }
    public Student[] getStudentsWithoutGrade() {
    // --- Primer recorrido: Contar ---
    int count = 0;
    Node current = first;
    while (current != null) {
        // Corrección 1: Definimos 'student' aquí también.
        Student student = current.value;
        if (student.grade == -1.0) {
            count++;
        }
        current = current.next;
    }

    // --- Segundo recorrido: Crear y rellenar ---
    Student[] studentsWithoutGrade = new Student[count];
    int index = 0;
    current = first; // Reiniciamos el recorrido
    while (current != null) {
        Student student = current.value;
        // Corrección 2: Usamos EXACTAMENTE la misma condición que antes.
        if (student.grade == -1.0) {
            studentsWithoutGrade[index] = student;
            index++;
        }
        current = current.next;
    }

    return studentsWithoutGrade;
}
}