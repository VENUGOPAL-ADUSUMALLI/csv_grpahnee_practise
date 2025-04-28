from django.contrib import admin

from .models import *

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Mark)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Book)

