from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [

    path('',views.Register,name='register'),
    path('log',views.Login1,name='log'),
    path('logout',views.Logout,name='logout'),

    path('home',views.index,name='index'),
    path('studentadd',views.StudentAdd,name="index1"),
    path('SRecords',views.Student_Records,name="record"),
    path("dele/<int:id>/",views.Delete_Student,name="student_Delete"),

    path('SCourseRecords',views.Student_Course_Records, name="course"),
    path('course_add',views.Student_Course_Add,name='student_course_add'),

    path('SAttendanceRecords',views.Student_Attendance_Records,name='attendance'),
    path("del/<int:id>/",views.Delete , name="delete"),
    path('Attendance_Add',views.Student_Attendance_ADD,name="Attendance_add")


    
]