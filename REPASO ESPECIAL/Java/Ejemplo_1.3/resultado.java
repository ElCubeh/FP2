public class Playlist extends PlaylistBase{
    private int totalTimePlayed = 0;
    private static int totalSongsPlayedGlobally = 0;

    public Song playSong(int index) {
    // Validación del índice
    if (index < 0 || index >= getSize()) {
        return null;
    }

    Song songRemoved;

    if (index == 0) {
        // --- Caso Especial: Eliminar el primer elemento ---
        songRemoved = first.value;
        first = first.next;
    } else {
        // --- Caso General: Eliminar un elemento del medio o final ---
        // 1. Encontramos el nodo ANTERIOR al que queremos eliminar.
        Node previous = first;
        for (int i = 0; i < index - 1; i++) {
            previous = previous.next;
        }

        // 2. 'previous' está en la posición correcta. El que queremos borrar es el siguiente.
        Node nodeToRemove = previous.next;
        songRemoved = nodeToRemove.value; // Guardamos la canción.

        // 3. Hacemos el "bypass". El .next del anterior apunta al .next del que borramos.
        previous.next = nodeToRemove.next;
    }

    // --- Pasos finales, comunes a ambos casos ---
    // 4. Actualizamos los contadores.
    this.totalTimePlayed += songRemoved.duration;
    Playlist.totalSongsPlayedGlobally++;

    // 5. Devolvemos la canción eliminada.
    return songRemoved;
}
    public int getTotalDurationLeft() {
    int totalDuration = 0; // Corregí el pequeño typo en "duration".
    Node current = first;

    while (current != null) {
        // 1. Obtenemos el objeto Song completo.
        Song song = current.value;

        // 2. Accedemos SOLO a su atributo 'duration' y lo sumamos al total.
        totalDuration += song.duration;

        current = current.next;
    }
    return totalDuration;
}

public Song[] getSongsByArtist(String artist) {
    // --- Primer recorrido: Contar (tu lógica, con la corrección) ---
    int count = 0;
    Node current = first;
    while (current != null) {
        // Usamos .equals() para comparar el contenido de los Strings
        if (current.value.artist.equals(artist)) {
            count++;
        }
        current = current.next;
    }

    // --- Segundo recorrido: Crear y rellenar el array ---
    Song[] songsByArtist = new Song[count];
    int index = 0;
    current = first; // Reiniciamos el recorrido
    while (current != null) {
        if (current.value.artist.equals(artist)) {
            songsByArtist[index] = current.value; // Guardamos la canción en el array
            index++;
        }
        current = current.next;
    }

    return songsByArtist;
}

public boolean moveSong(int fromIndex, int toIndex) {
    // 1. Validación de índices
    if (fromIndex < 0 || fromIndex >= getSize() || toIndex < 0 || toIndex >= getSize() || fromIndex == toIndex) {
        return false;
    }

    // --- Paso 2 y 3: Encontrar y desenganchar el nodo a mover ---
    Node nodeToMove;
    Node previousNode; // El nodo ANTERIOR al que vamos a mover

    if (fromIndex == 0) {
        // Caso especial: movemos el primer nodo
        nodeToMove = first;
        first = first.next; // Lo desenganchamos
        previousNode = null; // No hay anterior
    } else {
        // Buscamos el nodo anterior a 'fromIndex'
        previousNode = first;
        for (int i = 0; i < fromIndex - 1; i++) {
            previousNode = previousNode.next;
        }
        nodeToMove = previousNode.next;
        // Lo desenganchamos
        previousNode.next = nodeToMove.next;
    }

    // --- Paso 4 y 5: Encontrar el punto de inserción y reenganchar ---
    if (toIndex == 0) {
        // Caso especial: insertar al principio
        nodeToMove.next = first;
        first = nodeToMove;
    } else {
        // Buscamos el nodo anterior a 'toIndex'
        Node insertionPoint = first;
        // Ojo: el bucle es diferente si el 'toIndex' es mayor que el 'fromIndex'
        // porque la lista ha cambiado de tamaño en medio. Es más sencillo ajustar el índice.
        int adjustedToIndex = (toIndex > fromIndex) ? toIndex - 1 : toIndex;
        for (int i = 0; i < adjustedToIndex - 1; i++) {
            insertionPoint = insertionPoint.next;
        }
        // Reenganchamos el nodo
        nodeToMove.next = insertionPoint.next;
        insertionPoint.next = nodeToMove;
    }

    return true;
}