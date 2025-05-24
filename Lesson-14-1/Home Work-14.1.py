class GroupFullException(Exception):
    def __init__(self, message="Неможливо додати студента: група вже заповнена."):
        super().__init__(message)


class Student:
    def __init__(self, name, gender, age, record_book):
        self.name = name
        self.gender = gender
        self.age = age
        self.record_book = record_book

    def __str__(self):
        return f"{self.name}, {self.gender}, {self.age} y.o., Record Book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupFullException()
        self.students.append(student)

    def __str__(self):
        result = f"Number: {self.number}\n"
        for s in self.students:
            result += str(s) + "\n"
        return result.strip()


# --- Тестування ---
if __name__ == "__main__":
    group = Group("P01")

    for i in range(12):
        try:
            student = Student(f"Student{i+1}", "Any", 20+i, f"AN{i+100}")
            group.add_student(student)
            print(f"✅ Додано: {student}")
        except GroupFullException as e:
            print(f"❌ Помилка: {e}")
