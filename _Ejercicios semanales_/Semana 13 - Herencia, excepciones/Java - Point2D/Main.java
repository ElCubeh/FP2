public class Main {
    public static void main(String[] args) {
        Point2D point1 = new Point2D(10.0, 5.0);
        Point2D point2 = new Point2D(12.0, 5.0);
        String msg = point1.toString() + " " + point1.toString();
        msg += " " + (point1.equals(point2));
        System.out.println(msg);
    }
}