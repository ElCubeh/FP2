// Escriba aquí el código para definir la clase IntStack
import java.util.Objects;

public class IntStack extends IntContainer {
    
    public IntStack(int capacity) {
        data = new int[capacity];
        size = 0;
    }
    @Override
    public void insert(int value) throws CapacityOverflow {
        if (size >= data.length) {
            throw new CapacityOverflow("Contenedor lleno");
        }
        data[size] = value;
        size++;
    }
    @Override
    public String toString() {
        if (size == 0) return "{}";
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        for (int i = 0; i < size; i++) {
            sb.append(data[i]);
            if (i < size - 1) sb.append(" - ");
        }
        sb.append("}");
        return sb.toString();
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof IntStack)) return false;
        
        IntStack other = (IntStack) obj;
        if (this.size != other.size) return false;
        
        for (int i = 0; i < this.size; i++) {
            if (this.data[i] != other.data[i]) return false;
        }
        return true;
    }
}