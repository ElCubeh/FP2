public class Tools {
    public static int mcd(int a, int b) {
        return b == 0 ? Math.abs(a) : mcd(b, a % b);
    }
}
