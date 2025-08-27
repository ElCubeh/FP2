public class Catalog extends CatalogBase{
    private int checkedOutCount = 0;
    private static int totalLibraryLoans = 0;

// 1. El método devuelve un objeto 'Book'.
public Book checkoutBook(String isbn) {
    Node current = first; // Empezamos el recorrido.

    while (current != null) {
        Book book = current.value; // Obtenemos el libro del nodo actual.

        // 2. Comparamos el ISBN usando .equals()
        if (book.isbn.equals(isbn)) {
            // ¡Libro encontrado! Ahora comprobamos si está disponible.
            // 3. Verificamos si NO está prestado (!book.isCheckedOut).
            if (!book.isCheckedOut) {
                // Está disponible, ¡lo prestamos!
                book.isCheckedOut = true;      // Actualizamos su estado.
                this.checkedOutCount++;        // Actualizamos el contador de esta biblioteca.
                Catalog.totalLibraryLoans++;   // Actualizamos el contador global.

                return book; // Devolvemos el libro que acabamos de prestar.
            } else {
                // El libro existe pero ya está prestado. No podemos hacer nada.
                // Devolvemos null y salimos.
                return null;
            }
        }
        current = current.next; // Pasamos al siguiente libro.
    }

    // 4. Si el bucle termina, es que el libro no existe en el catálogo.
    return null;
}
// 1. Cambiamos el tipo de retorno a 'void'.
public void returnBook(String isbn) {
    Node current = first;
    while (current != null) {
        Book book = current.value;
        if (book.isbn.equals(isbn)) {
            // Comprobamos si el libro estaba realmente prestado.
            if (book.isCheckedOut) {
                book.isCheckedOut = false; // 2. Añadimos el punto y coma.
                this.checkedOutCount--;
            }
            // 3. Salimos del método porque ya hemos encontrado el libro.
            return;
        }
        current = current.next;
    }
}

public Book[] getAvailableBooks() {
    // --- Primer recorrido: Contar (esto lo hiciste perfecto) ---
    int count = 0;
    Node current = first;
    while (current != null) {
        Book book = current.value;
        if (!book.isCheckedOut) {
            count++;
        }
        current = current.next;
    }

    // --- Segundo recorrido: Crear y rellenar ---
    // (He cambiado el nombre del array a algo más descriptivo)
    Book[] availableBooks = new Book[count];
    int index = 0;
    current = first; // Reiniciamos el recorrido

    while (current != null) {
        Book book = current.value;
        if (!book.isCheckedOut) {
            // ¡Esta es la línea que faltaba!
            // Guardamos el libro encontrado en la posición actual del array.
            availableBooks[index] = book;
            index++; // Y luego avanzamos el índice.
        }
        current = current.next;
    }

    // ¡Y esta es la otra línea que faltaba!
    // Devolvemos el array ya completo.
    return availableBooks;
}

public int countBooksByAuthor(String author) {
    Node current = first;
    int count = 0;

    while (current != null) {
        Book book = current.value;
        // 1 y 2: Accedemos a book.author y comparamos con .equals()
        if (book.author.equals(author)) {
            count++; // 3. Añadimos el punto y coma
        }
        current = current.next;
    }
    return count;
}