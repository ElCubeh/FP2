/**
 * La clase PostFeed gestiona un feed de publicaciones de una red social.
 * Hereda de FeedBase para la funcionalidad básica de la lista.
 */
public class PostFeed extends FeedBase {

    // --- ATRIBUTOS ---

    /**
     * Almacena la suma de todos los "likes" de las publicaciones en ESTE feed.
     */
    private int totalLikesInFeed = 0;

    /**
     * Contador estático para el total de publicaciones eliminadas en TODOS los feeds.
     */
    private static int totalPostsDeleted = 0;

    // --- MÉTODOS IMPLEMENTADOS ---

    /**
     * Incrementa el contador de "likes" de una publicación.
     *
     * @param postId El ID de la publicación a la que dar "like".
     * @return true si se encontró y actualizó, false en caso contrario.
     */
    public boolean likePost(int postId) {
        Node current = first;
        while (current != null) {
            if (current.value.postId == postId) {
                current.value.likes++;
                this.totalLikesInFeed++;
                return true;
            }
            current = current.next;
        }
        return false;
    }

    /**
     * Encuentra y devuelve la publicación con más "likes" del feed.
     *
     * @return El Post con más "likes", o null si el feed está vacío.
     */
    public Post getMostLikedPost() {
        if (first == null) {
            return null;
        }
        Post mostLiked = first.value;
        Node current = first.next;
        while (current != null) {
            if (current.value.likes > mostLiked.likes) {
                mostLiked = current.value;
            }
            current = current.next;
        }
        return mostLiked;
    }

    /**
     * Elimina una publicación del feed.
     *
     * @param postId El ID de la publicación a eliminar.
     * @return El Post eliminado, o null si no se encontró.
     */
    public Post deletePost(int postId) {
        if (first == null) return null;

        Post postDeleted;

        if (first.value.postId == postId) {
            postDeleted = first.value;
            first = first.next;
        } else {
            Node previous = first;
            Node current = first.next;
            while (current != null) {
                if (current.value.postId == postId) {
                    postDeleted = current.value;
                    previous.next = current.next;
                    // Actualizar contadores y devolver
                    this.totalLikesInFeed -= postDeleted.likes;
                    PostFeed.totalPostsDeleted++;
                    return postDeleted;
                }
                previous = current;
                current = current.next;
            }
            return null; // No se encontró.
        }

        // Actualizar contadores si se borró el primero.
        this.totalLikesInFeed -= postDeleted.likes;
        PostFeed.totalPostsDeleted++;
        return postDeleted;
    }

    /**
     * Devuelve un array con todas las publicaciones de un autor específico.
     *
     * @param author El autor a buscar.
     * @return Un array de objetos Post.
     */
    public Post[] getPostsByAuthor(String author) {
        int count = 0;
        Node current = first;
        while (current != null) {
            if (current.value.author.equals(author)) {
                count++;
            }
            current = current.next;
        }

        Post[] authorPosts = new Post[count];
        int index = 0;
        current = first;
        while (current != null) {
            if (current.value.author.equals(author)) {
                authorPosts[index] = current.value;
                index++;
            }
            current = current.next;
        }
        return authorPosts;
    }
}
