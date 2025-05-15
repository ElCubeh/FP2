import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Point3D point1 = new Point3D(10.0, 5.0, 8.5);
        Point3D point2 = new Point3D(10.0, 3.0, 8.5);
        System.out.println(point1);
        System.out.println(point1.equals(point2));
        System.out.println(Arrays.toString(point1.coordinates()));
    }
}