/**
 * =================================================================
 * PATRÓN 1: RECORRIDO PARA CÁLCULO (CONTEO O SUMA)
 * =================================================================
 *
 * OBJETIVO:
 * Recorrer una lista enlazada de principio a fin para:
 * a) Contar cuántos elementos cumplen una condición.
 * b) Sumar un valor numérico de cada elemento que cumple una condición.
 *
 * ESTRUCTURA GENÉRICA:
 */
public class EstructuraGenerica {

    // El tipo de retorno (int, double, etc.) y los parámetros dependen del problema.
    public double metodoDeCalculo(/* ... parámetros con condiciones ... */) {
        // 1. Inicializa una variable "acumulador" a cero.
        double acumulador = 0.0;

        // 2. Crea un puntero 'current' que apunta al inicio de la lista.
        Node current = first;

        // 3. Bucle 'while' que se ejecuta mientras no lleguemos al final.
        while (current != null) {
            // Se obtiene el objeto del nodo actual.
            Objeto miObjeto = current.value;

            // 4. (Opcional) Condición 'if' para filtrar los elementos a procesar.
            if (/* miObjeto cumple la condición de búsqueda */) {
                // 5. Se actualiza el acumulador.
                //    - Para contar: acumulador++;
                //    - Para sumar: acumulador += miObjeto.valorNumerico;
            }

            // 6. ¡CRÍTICO! Se avanza al siguiente nodo para no crear un bucle infinito.
            current = current.next;
        }

        // 7. ¡CRÍTICO! Se devuelve el resultado final DESPUÉS de que el bucle termine.
        return acumulador;
    }
}

/*
 * =================================================================
 * EJEMPLO 1: CONTEO (Aplicado al Ejercicio 8: Sistema de Votación)
 * =================================================================
 * Objetivo: Contar los votos para un candidato específico.
 */
class EjemploConteo {
    /**
     * Cuenta los votos para un candidato específico.
     * @param candidateName El nombre del candidato a buscar.
     * @return El número de votos.
     */
    public int countVotesFor(String candidateName) {
        // 1. Inicializa el acumulador (contador).
        int voteCount = 0;
        // 2. Empieza el recorrido.
        Node current = first;
        // 3. Bucle 'while'.
        while (current != null) {
            Vote vote = current.value;
            // 4. Condición de filtrado.
            if (vote.candidateName.equals(candidateName)) {
                // 5. Actualiza el acumulador (contando).
                voteCount++;
            }
            // 6. Avanza al siguiente.
            current = current.next;
        }
        // 7. Devuelve el resultado final.
        return voteCount;
    }
}

/*
 * =================================================================
 * EJEMPLO 2: SUMA (Aplicado al Ejercicio 3: Playlist de Música)
 * =================================================================
 * Objetivo: Sumar las duraciones de todas las canciones restantes.
 */
class EjemploSuma {
    /**
     * Calcula la duración total restante de la playlist.
     * @return El total de segundos.
     */
    public int getTotalDurationLeft() {
        // 1. Inicializa el acumulador (suma).
        int totalDuration = 0;
        // 2. Empieza el recorrido.
        Node current = first;
        // 3. Bucle 'while'.
        while (current != null) {
            Song song = current.value;
            // 4. No hay condición 'if', se incluyen todas las canciones.
            // 5. Actualiza el acumulador (sumando).
            totalDuration += song.duration;
            // 6. Avanza al siguiente.
            current = current.next;
        }
        // 7. Devuelve el resultado final.
        return totalDuration;
    }
}



/**
 * =================================================================
 * PATRÓN 2: BÚSQUEDA DEL "MEJOR" ELEMENTO (ALGORITMO DEL CAMPEÓN)
 * =================================================================
 *
 * OBJETIVO:
 * Recorrer una lista para encontrar un único elemento que sea el "mejor"
 * según un criterio numérico (el máximo, el mínimo, el más largo, etc.).
 *
 * ESTRUCTURA GENÉRICA:
 */
public class EstructuraGenerica {

    // Devuelve el tipo de objeto que estamos buscando.
    public Objeto encontrarElMejor() {
        // 1. Si la lista está vacía, no hay campeón, devolvemos null.
        if (first == null) {
            return null;
        }

        // 2. Asumimos que el PRIMER elemento es el "campeón actual" para empezar.
        Objeto campeonActual = first.value;
        // (Opcional) Guardamos su récord para comparar más fácil.
        double recordABatir = campeonActual.valorNumerico;

        // 3. Empezamos el recorrido desde el SEGUNDO elemento.
        Node current = first.next;

        // 4. Recorremos el resto de la lista.
        while (current != null) {
            Objeto competidor = current.value;

            // 5. ¡CRÍTICO! Comparamos el "competidor" actual con nuestro "récord".
            //    - Para buscar el MÁXIMO: if (competidor.valorNumerico > recordABatir)
            //    - Para buscar el MÍNIMO: if (competidor.valorNumerico < recordABatir)
            if (/* el competidor supera el récord */) {
                // ¡Tenemos un nuevo campeón!
                // 6. Actualizamos tanto al campeón como el récord.
                campeonActual = competidor;
                recordABatir = competidor.valorNumerico;
            }

            // 7. Avanzamos al siguiente competidor.
            current = current.next;
        }

        // 8. Devolvemos al campeón definitivo que ha sobrevivido a todas las comparaciones.
        return campeonActual;
    }
}

/*
 * =================================================================
 * EJEMPLO 1: BÚSQUEDA DE MÁXIMO (Aplicado al Ejercicio 14: Red Social)
 * =================================================================
 * Objetivo: Encontrar la publicación con el mayor número de "likes".
 */
class EjemploMaximo {
    public Post getMostLikedPost() {
        if (first == null) return null;

        // 1. El primer post es nuestro campeón inicial.
        Post mostLiked = first.value;
        // 2. El récord a batir es su número de likes.
        int maxLikes = mostLiked.likes;

        // 3. Empezamos a comparar desde el segundo post.
        Node current = first.next;
        while (current != null) {
            Post currentPost = current.value;
            // 4. Condición de búsqueda de máximo.
            if (currentPost.likes > maxLikes) {
                // 5. ¡Nuevo campeón encontrado! Actualizamos todo.
                mostLiked = currentPost;
                maxLikes = currentPost.likes;
            }
            current = current.next;
        }
        return mostLiked;
    }
}

/*
 * =================================================================
 * EJEMPLO 2: BÚSQUEDA DE MÍNIMO (Aplicado al Ejercicio 6: Banco)
 * =================================================================
 * Objetivo: Encontrar el retiro más grande (el 'amount' negativo más bajo).
 */
class EjemploMinimo {
    public Transaction getLargestWithdrawal() {
        // 1. Campeón inicial es null, no hemos visto ningún retiro.
        Transaction largestWithdrawal = null;
        // 2. Récord inicial es 0. Cualquier número negativo será menor.
        double lowestAmount = 0.0;

        // 3. Empezamos el recorrido desde el principio.
        Node current = first;
        while (current != null) {
            Transaction tx = current.value;
            // Solo nos interesan los retiros (amount < 0).
            if (tx.amount < 0) {
                // 4. Condición de búsqueda de mínimo.
                if (tx.amount < lowestAmount) {
                    // 5. ¡Nuevo campeón! Actualizamos todo.
                    largestWithdrawal = tx;
                    lowestAmount = tx.amount;
                }
            }
            current = current.next;
        }
        return largestWithdrawal;
    }
}




/**
 * =================================================================
 * PATRÓN 3: FILTRADO Y CREACIÓN DE UN ARRAY (CONTAR Y RELLENAR)
 * =================================================================
 *
 * OBJETIVO:
 * Seleccionar todos los elementos de la lista que cumplen una condición
 * y devolverlos en un array del tamaño exacto.
 *
 * ESTRUCTURA GENÉRICA:
 */
public class EstructuraGenerica {

    // Devuelve un array del objeto que estamos buscando, ej: Objeto[]
    public Objeto[] filtrarElementos(/* ... parámetros con condiciones ... */) {
        // === PASO 1: PRIMER RECORRIDO PARA CONTAR ===
        int count = 0;
        Node current = first;
        while (current != null) {
            if (/* el objeto en current.value cumple la condición */) {
                count++;
            }
            current = current.next;
        }

        // === PASO 2: SEGUNDO RECORRIDO PARA CREAR Y RELLENAR ===

        // 1. Se crea el array con el tamaño exacto que se acaba de contar.
        Objeto[] resultado = new Objeto[count];
        int index = 0; // Índice para saber dónde insertar en el array 'resultado'.

        // 2. ¡CRÍTICO! Se reinicia el puntero 'current' para volver a empezar.
        current = first;

        // 3. Bucle 'while' para el segundo recorrido.
        while (current != null) {
            // 4. ¡CRÍTICO! Se usa EXACTAMENTE la misma condición 'if' que antes.
            if (/* el objeto en current.value cumple la condición */) {
                // 5. Se añade el objeto al array y se avanza el índice del array.
                resultado[index] = current.value;
                index++;
            }
            current = current.next;
        }

        // 6. Se devuelve el array ya completo.
        return resultado;
    }
}

/*
 * =================================================================
 * EJEMPLO 1 (Aplicado al Ejercicio 10: Log de Errores)
 * =================================================================
 * Objetivo: Obtener todos los errores con prioridad "HIGH".
 */
class EjemploErrorLog {
    public AppError[] getHighPriorityErrors() {
        // --- Contar ---
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.priority.equals("HIGH")) {
                count++;
            }
            current = current.next;
        }

        // --- Rellenar ---
        AppError[] highPriorityErrors = new AppError[count];
        int index = 0;
        current = first; // Reiniciar
        while (current != null) {
            if (current.value.priority.equals("HIGH")) {
                highPriorityErrors[index++] = current.value;
            }
            current = current.next;
        }
        return highPriorityErrors;
    }
}

/*
 * =================================================================
 * EJEMPLO 2 (Aplicado al Ejercicio 13: Flota de Coches)
 * =================================================================
 * Objetivo: Obtener todos los coches que no están alquilados.
 */
class EjemploFlotaCoches {
    public RentalCar[] getAvailableCars() {
        // --- Contar ---
        int count = 0;
        Node current = first;
        while (current != null) {
            if (!current.value.isRented) { // Condición: isRented es false
                count++;
            }
            current = current.next;
        }

        // --- Rellenar ---
        RentalCar[] availableCars = new RentalCar[count];
        int index = 0;
        current = first; // Reiniciar
        while (current != null) {
            if (!current.value.isRented) {
                availableCars[index++] = current.value;
            }
            current = current.next;
        }
        return availableCars;
    }
}





/**
 * =================================================================
 * PATRÓN 4: ELIMINACIÓN DE UN ÚNICO NODO
 * =================================================================
 *
 * OBJETIVO:
 * Encontrar un elemento específico en la lista (por ID, nombre, etc.)
 * y eliminarlo, reajustando los punteros de la lista.
 *
 * ESTRUCTURA GENÉRICA:
 */
public class EstructuraGenerica {

    // Devuelve el objeto que se ha eliminado.
    public Objeto eliminarElemento(TIPO_DE_DATO identificador) {
        // Si la lista está vacía, no hay nada que hacer.
        if (first == null) {
            return null;
        }

        // === PASO 1: CASO ESPECIAL - El nodo a eliminar es el PRIMERO ===
        if (/* el objeto en 'first.value' coincide con el identificador */) {
            Objeto objetoEliminado = first.value; // 1. Guardamos el objeto.
            first = first.next;                   // 2. Lo eliminamos moviendo el puntero 'first'.
            // (Aquí irían actualizaciones de contadores si es necesario)
            return objetoEliminado;
        }

        // === PASO 2: CASO GENERAL - El nodo está en el medio o al final ===

        // 1. Se necesitan dos punteros: 'previous' (anterior) y 'current' (actual).
        Node previous = first;
        Node current = first.next;

        // 2. Se recorre el resto de la lista.
        while (current != null) {
            if (/* el objeto en 'current.value' coincide con el identificador */) {
                // ¡Lo encontramos!
                Objeto objetoEliminado = current.value; // Guardamos el objeto.
                // 3. ¡CRÍTICO! Hacemos el "bypass": el anterior se salta al actual.
                previous.next = current.next;
                // (Aquí irían actualizaciones de contadores)
                return objetoEliminado;
            }
            // 4. Si no es el que buscamos, avanzamos AMBOS punteros.
            previous = current;
            current = current.next;
        }

        // 5. Si el bucle termina, significa que no se encontró el elemento.
        return null;
    }
}

/*
 * =================================================================
 * EJEMPLO 1 (Aplicado al Ejercicio 7: Planificador de Eventos)
 * =================================================================
 * Objetivo: Cancelar un evento buscándolo por su nombre.
 */
class EjemploPlanificador {
    public Event cancelEvent(String eventName) {
        if (first == null) return null;

        // Caso especial: es el primer evento.
        if (first.value.eventName.equals(eventName)) {
            Event cancelled = first.value;
            first = first.next;
            // Actualizar contadores...
            return cancelled;
        }

        // Caso general: está en el medio o al final.
        Node previous = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.eventName.equals(eventName)) {
                Event cancelled = current.value;
                previous.next = current.next;
                // Actualizar contadores...
                return cancelled;
            }
            previous = current;
            current = current.next;
        }
        return null;
    }
}




/**
 * =================================================================
 * PATRÓN 5: ELIMINACIÓN MÚLTIPLE DE NODOS
 * =================================================================
 *
 * OBJETIVO:
 * Recorrer la lista y eliminar TODOS los nodos que cumplan una condición.
 * Es más complejo que la eliminación simple por el manejo de los punteros.
 *
 * ESTRUCTURA GENÉRICA:
 */
public class EstructuraGenerica {

    // Devuelve el número de elementos que se han eliminado.
    public int eliminarMultiplesElementos() {
        int eliminadosCount = 0;

        // === PASO 1: CASO ESPECIAL - Eliminar desde el principio de la lista ===
        // Se usa un 'while' por si hay varios nodos seguidos que cumplen la condición.
        while (first != null && /* el objeto en first.value cumple la condición */) {
            first = first.next;
            eliminadosCount++;
        }

        // Si la lista se quedó vacía, hemos terminado.
        if (first == null) {
            return eliminadosCount;
        }

        // === PASO 2: CASO GENERAL - Eliminar del resto de la lista ===
        Node previous = first;
        Node current = first.next;

        while (current != null) {
            if (/* el objeto en current.value cumple la condición */) {
                // 1. Lo eliminamos. ¡'previous' NO se mueve!
                previous.next = current.next;
                eliminadosCount++;
            } else {
                // 2. Si NO lo eliminamos, 'previous' SÍ avanza.
                previous = current;
            }
            // 3. 'current' siempre avanza al siguiente nodo válido de la lista modificada.
            current = previous.next;
        }

        return eliminadosCount;
    }
}

/*
 * =================================================================
 * EJEMPLO 1 (Aplicado al Ejercicio 17: Gimnasio)
 * =================================================================
 * Objetivo: Eliminar a todos los miembros con menos de 'minVisits' visitas.
 */
class EjemploGimnasio {
    public int removeInactiveMembers(int minVisits) {
        int removedCount = 0;
        
        // Eliminar inactivos desde el principio.
        while (first != null && first.value.visits < minVisits) {
            first = first.next;
            removedCount++;
        }

        if (first == null) return removedCount;

        // Eliminar inactivos del resto.
        Node previous = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.visits < minVisits) {
                // Eliminar: 'previous' se queda quieto.
                previous.next = current.next;
                removedCount++;
            } else {
                // No eliminar: 'previous' avanza.
                previous = current;
            }
            // 'current' avanza al siguiente de 'previous'.
            current = previous.next;
        }
        return removedCount;
    }
}
