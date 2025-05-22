/**
 * Clase base para un contenedor de enteros
 * NO MODIFICAR: No tiene efecto
 */
public abstract class IntContainer {
    protected int[] data;
    protected int size;

    public abstract void insert(int value) throws CapacityOverflow;
}
