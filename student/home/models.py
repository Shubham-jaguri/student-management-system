from django.db import models

# Create your models here.
class Student_Add(models.Model):
    roll_no = models.CharField( max_length=10,primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    gender= models.CharField(max_length=10)
    birth= models.CharField(max_length=10)
    course= models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    
class Student_Course(models.Model):
    course_id = models.CharField(max_length=10,primary_key=True,unique=True)
    course_name=models.CharField(max_length=40)
    course_code=models.CharField(max_length=10)
    department= models.CharField(max_length=40)
    duration = models.CharField(max_length=20)
    semester= models.CharField(max_length=20)
    Instructor=models.CharField(max_length=20)
    fees= models.CharField(max_length=20)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student_Add, on_delete=models.CASCADE)
    course = models.ForeignKey(Student_Course, on_delete=models.CASCADE)

class Student_Attendence(models.Model):
    Roll_no=models.CharField(max_length=10)
    student_name=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    attendance=models.CharField(max_length=20)