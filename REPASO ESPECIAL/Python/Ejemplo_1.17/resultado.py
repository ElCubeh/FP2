class Student:
    def __init__(self, student_id, name, grade=0.0):
        self.student_id = student_id
        self.name = name
        self.grade = grade

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CourseBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def enroll_student(self, student):
        new_node = Node(student)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class Course(CourseBase):
    _total_enrollment = 0
    
    def enroll_student(self, student):
        super().enroll_student(student)
        Course._total_enrollment += 1

    def drop_student(self, student_id):
        prev, curr = None, self.first
        while curr:
            if curr.value.student_id == student_id:
                if prev is None: self.first = curr.next
                else: prev.next = curr.next
                self._size -= 1
                Course._total_enrollment -= 1
                return curr.value
            prev, curr = curr, curr.next
        return None

    def record_grade(self, student_id, new_grade):
        curr = self.first
        while curr:
            if curr.value.student_id == student_id:
                curr.value.grade = new_grade
                return True
            curr = curr.next
        return False

    @property
    def class_average(self):
        if self.get_size() == 0:
            return 0.0
        total_grade = 0
        curr = self.first
        while curr:
            total_grade += curr.value.grade
            curr = curr.next
        return total_grade / self.get_size()

    @classmethod
    def get_total_enrollment(cls):
        return cls._total_enrollment