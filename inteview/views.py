import csv

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from inteview.models import *


# Create your views here.
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def create_resources_view(request):
    department = request.data.get("department")
    name = request.data.get("name")
    age = request.data.get("age")
    create_department = Department.objects.create(name=department)
    create_student = Student.objects.create(name=name, age=age, department=create_department)
    return create_student


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def export_to_csv(request):
    books = Book.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment ; filename=books_export_data.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages', 'rating_count',
         'text_review_count', 'publication_date', 'publisher'])
    books_files = books.values_list('title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code',
                                    'num_pages', 'rating_count',
                                    'text_review_count', 'publication_date', 'publisher')
    for each_book in books_files:
        writer.writerow(each_book)
    return response


from rest_framework.response import Response


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def get_queries(request):
    name = request.data.get("name")
    category = Category.objects.filter(name=name).first()

    if not category:
        return Response({"error": "Category not found"}, status=404)

    ingredients = Ingredient.objects.filter(category=category)

    # Build a list of ingredients info
    ingredients_list = []
    for ingredient in ingredients:
        ingredients_list.append({
            "ingredient_name": ingredient.name,
            "category_name": ingredient.category.name
        })

    return Response({"ingredients": ingredients_list})
