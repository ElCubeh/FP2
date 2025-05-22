
public class ChildListOfInt extends ListOfInt {

    public int getLength() {
        int count = 0;
        Node current = first;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

    @Override
    public String toString() {
        return "(" + getLength() + ")" + super.toString();
    }
}
