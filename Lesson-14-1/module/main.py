from student import Student
from group import Group
from exceptions import GroupFullException

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

# --- Перевірки ---
assert gr.find_student('Jobs') == st1, 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'

gr.delete_student('Taylor')
print(gr)  # Лише один студент

# Повторне видалення — без помилки
gr.delete_student('Taylor')
