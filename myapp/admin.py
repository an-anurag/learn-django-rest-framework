from django.contrib import admin
from .models import StudentModel, SchoolModel, StandardModel
# Register your models here.


admin.site.register(StandardModel)
admin.site.register(SchoolModel)
admin.site.register(StudentModel)