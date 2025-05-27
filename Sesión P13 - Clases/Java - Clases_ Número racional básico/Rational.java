public class Rational {
    private int num;
    private int den;
    public Rational(int num,int den) {
        if (den < 0) {
            num = -num;
            den = -den;
        }
        int gcd = Tools.mcd(Math.abs(num), den);
        this.num = num / gcd;
        this.den = den / gcd;
    }
    public Rational add(Rational other) {
        int newNum = this.num * other.den + other.num * this.den;
        int newDen = this.den * other.den;
        return new Rational(newNum, newDen);
    }
    public Rational prod(Rational other) {
        int newNum = this.num * other.num;
        int newDen = this.den * other.den;
        return new Rational(newNum, newDen);
    }
    @Override
    public String toString() {
        return this.num + " / " + this.den;
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Rational)) return false;
        Rational other = (Rational) obj;
        return this.num == other.num && this.den == other.den;
    }
}