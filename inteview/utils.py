from django.db.models import Sum
from .models import *

total_marks = Student.objects.annotate(total_marks=Sum('mark__marks_obtained'))
total_marks_aggregate = Mark.objects.aggregate(total_marks=Sum('marks_obtained'))

print(total_marks)
print(total_marks_aggregate)

cse_department = Department.objects.get(name='CSE')
students_in_cse = cse_department.student_set.all()

for student in students_in_cse:
    print(student.name)
# for optimizing queries we will use select_related and prefetch_related
students = Student.objects.select_related('department').all()

for student in students:
    print(student.name, student.department.name)
create_department = Department.objects.create(name="CIVIL")
create_student = Student.objects.create(name="Vajrao", age=20, department=create_department)
print(create_student)
