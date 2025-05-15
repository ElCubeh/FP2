public class Main {
    public static void main(String[] args) {
        Point2DComparable point1 = new Point2DComparable(10.0, 5.0);
        Point2DComparable point2 = new Point2DComparable(12.0, 5.0);
        System.out.println(point1.compareTo(point2));
    }
}