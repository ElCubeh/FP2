/** Clase que representa un rectángulo definido por dos puntos: 
 *  el inferior izquierdo y el superior derecho */
public class Rectangulo {
    private Punto ptoInfIzq;
    private Punto ptoSupDer;

    public Rectangulo(Punto ptoInfIzq, Punto ptoSupDer) {
        this.ptoInfIzq = ptoInfIzq;
        this.ptoSupDer = ptoSupDer;
    }
    public double base() {
        return ptoSupDer.getX() - ptoInfIzq.getX();
    }
    public double altura() {
        return ptoSupDer.getY() - ptoInfIzq.getY();
    }
    public double perimetro(){
        return 2 * (base() + altura());
    }
    public void reescalar(double factor) {
        double baseNueva = base() * factor;
        double alturaNueva = altura() * factor;
        ptoSupDer = new Punto (
            ptoInfIzq.getX() + baseNueva,
            ptoInfIzq.getY() + alturaNueva
        );
    }
    @Override
    public String toString() {
        return "<" + ptoInfIzq.toString() + ", " + ptoSupDer.toString() + ">";
    }
}
