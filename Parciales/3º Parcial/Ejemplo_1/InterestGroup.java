// Desarrolle aquí su código
class InterestGroup extends ContainerBase {
    private int size;

    public InterestGroup() {
        size = 0;
    }

    public boolean isMember(String name) {
        Node current = first;
        while (current != null) {
            if (current.value.equals(name)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    public boolean addMember(String name) {
        if (isMember(name)) {
            return false;
        }
        Node newNode = new Node();
        newNode.value = name;
        newNode.next = first;
        first = newNode;
        size++;
        return true;
    }

    public int getSize() {
        return size;
    }

    public InterestGroup union(InterestGroup other) {
        InterestGroup newGroup = new InterestGroup();
        Node current = this.first;
        while (current != null) {
            newGroup.addMember(current.value);
            current = current.next;
        }
        current = other.first;
        while (current != null) {
            newGroup.addMember(current.value);
            current = current.next;
        }
        return newGroup;
    }

    public boolean removeMember(String name) {
        if (first == null) {
            return false;
        }
        if (first.value.equals(name)) {
            first = first.next;
            size--;
            return true;
        }
        Node prev = first;
        Node current = first.next;
        while (current != null) {
            if (current.value.equals(name)) {
                prev.next = current.next;
                size--;
                return true;
            }
            prev = current;
            current = current.next;
        }
        return false;
    }
}