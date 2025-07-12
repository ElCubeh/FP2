public class Pruebas {
    public static void main (String[] args) {
        CheckoutQueue cola = new CheckoutQueue();
        System.out.println(cola);             // ➡️null⬅️
        cola.enqueue(new Client("Ana", 35));
        cola.enqueue(new Client("Luis", 50));
        cola.enqueue(new Client("Marta", 25));
        System.out.println(cola);             // ➡️[Ana: 35]->[Luis: 50]->[Marta: 25]⬅️->null
        System.out.println(cola.dequeue());   // Ana: 35
        System.out.println(cola.dequeue());   // Luis: 50
        System.out.println(cola.getDailySales()); // 85
        System.out.println(cola);  
    }
}