import java.util.Arrays;

// Escriba su código aquí
public class Point3D extends Point2D {
    protected double z;

    public Point3D(double x, double y, double z) {
        super(x, y);
        this.z = z;
    }

    @Override
    public double[] coordinates() {
        return new double[]{x, y, z};
    }

    @Override
    public boolean equals(Object other) {
        if (other instanceof Point3D) {
            Point3D p = (Point3D) other;
            return super.equals(p) && this.z == p.z;
        }
        return false;
    }

    @Override
    public String toString() {
        return super.toString() + ", z: " + z;
    }
}

