// Desarrolle aquí su código
public class CheckoutQueue extends ContainerBase {
    private double dailySales;

    public CheckoutQueue() {
        super();
        dailySales = 0.0;
    }

    public void enqueue(Client client) {
        Node newNode = new Node(client);
        if (first == null) {
            first = newNode;
            last = newNode;
        } else {
            last.next = newNode;
            last = newNode;
        }
    }

    public Client dequeue() {
        if (first == null) {
            return null;
        }
        Client client = first.value;
        first = first.next;
        if (first == null) {
            last = null;
        }
        dailySales += client.totalCost;
        return client;
    }

    public double getDailySales() {
        return dailySales;
    }

    public CheckoutQueue split() {
        CheckoutQueue oddQueue = new CheckoutQueue();
        if (first == null) {
            return oddQueue;
        }

        Node evenTail = null;
        Node current = first;
        int index = 0;

        while (current != null) {
            if (index % 2 == 0) {
                evenTail = current;
                current = current.next;
                index++;
            } else {
                Node oddNode = current;
                current = current.next;
                
                if (evenTail != null) {
                    evenTail.next = current;
                }
                
                if (oddQueue.first == null) {
                    oddQueue.first = oddNode;
                    oddQueue.last = oddNode;
                } else {
                    oddQueue.last.next = oddNode;
                    oddQueue.last = oddNode;
                }
                oddNode.next = null;
                index++;
            }
        }
        
        last = evenTail;
        return oddQueue;
    }
}