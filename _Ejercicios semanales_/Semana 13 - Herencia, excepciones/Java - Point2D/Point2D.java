import java.util.Arrays;

public class Point2D {
	protected double x, y;
    
    public Point2D(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    public double[] coordinates() {
        return new double[]{x, y};
    }
    
    @Override
    public boolean equals(Object other) {
        if (other instanceof Point2D) {
            Point2D p = (Point2D) other;
            return this.x == p.x && this.y == p.y;
        } else {
            return false;
        }
    }
    
    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}
