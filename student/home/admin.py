from django.contrib import admin

# Register your models here.
from .models import Student_Add
from .models import Student_Course
from .models import StudentCourse
from .models import Student_Attendence



admin.site.register(Student_Add)
admin.site.register(Student_Course)
admin.site.register(StudentCourse)
admin.site.register(Student_Attendence)
