// Desarrolle aquí su código
public class TaskList extends TaskListBase {
    private int timeSpent;
    private static int totalTimeSpent = 0;

    public TaskList() {
        super();
        this.timeSpent = 0;
    }

    public Task taskCompleted(int index) {
        if (index < 0 || first == null) {
            return null;
        }
        
        Node current = first;
        Node prev = null;
        int count = 0;
        
        while (current != null && count != index) {
            prev = current;
            current = current.next;
            count++;
        }
        
        if (current == null) {
            return null;
        }
        
        Task completedTask = current.value;
        int duration = completedTask.duration;
        
        if (prev == null) {
            first = first.next;
        } else {
            prev.next = current.next;
        }
        
        timeSpent += duration;
        totalTimeSpent += duration;
        return completedTask;
    }

    public int getTimeLeft() {
        int total = 0;
        Node current = first;
        while (current != null) {
            total += current.value.duration;
            current = current.next;
        }
        return total;
    }

    public int getTimeSpent() {
        return timeSpent;
    }

    public static int getTotalTimeSpent() {
        return totalTimeSpent;
    }

    public Task[] getTaskArray() {
        int size = getSize();
        Task[] tasks = new Task[size];
        Node current = first;
        int index = 0;
        while (current != null) {
            tasks[index++] = current.value;
            current = current.next;
        }
        return tasks;
    }
}