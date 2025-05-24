from exceptions import GroupFullException

class Group:
    def __init__(self, number):
        self.number = number
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupFullException()
        self.students.add(student)

    def find_student(self, surname):
        for s in self.students:
            if s.surname == surname:
                return s
        return None

    def delete_student(self, surname):
        student = self.find_student(surname)
        if student:
            self.students.remove(student)

    def __str__(self):
        result = f"Number: {self.number}\n"
        for s in self.students:
            result += str(s) + "\n"
        return result.strip()
