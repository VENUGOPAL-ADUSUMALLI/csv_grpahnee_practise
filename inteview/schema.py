import graphene
from graphene_django import DjangoObjectType

from .models import *


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = ("user", "cabin_name", "start_time", "end_time")


class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        fields = ("id", "name")


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "age", "department")


class MarkType(DjangoObjectType):
    class Meta:
        model = Mark
        fields = ("id", "student", "subject", "marks_obtained")


class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject
        fields = ("id", "name", "department")


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.List(CategoryType, name=graphene.String(required=True))
    all_department = graphene.List(DepartmentType)
    student_by_department = graphene.List(StudentType, department=graphene.String(required=True))
    marks_by_student_name = graphene.List(MarkType, student=graphene.String(required=True))
    all_subjects = graphene.List(SubjectType)

    def resolve_all_subjects(root, info):
        return Subject.objects.select_related("department").all()

    def resolve_all_department(root, info):
        return Department.objects.all()

    def resolve_student_by_department(root, info, department):
        return Student.objects.filter(department__name=department)

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        return Category.objects.filter(name=name)

    def resolve_marks_by_student_name(root, info, student):
        return Mark.objects.filter(student__name=student)


schema = graphene.Schema(query=Query)
