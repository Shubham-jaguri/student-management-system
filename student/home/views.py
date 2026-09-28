from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Student_Add,Student_Course,StudentCourse,Student_Attendence
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index1.html')


#STUDENT ADD,RECORDS,DELETE
def StudentAdd(request):
    if request.method =="POST":
        Sroll_no = request.POST.get("roll")
        Sname = request.POST.get("name")
        Semail = request.POST.get("email")
        Sphone = request.POST.get("phone")
        Sgender = request.POST.get("gender")
        Sdatebrith = request.POST.get("date")
        Scourse = request.POST.get("course")
        Saddress = request.POST.get("address")
        query1 = Student_Add(roll_no=Sroll_no,name=Sname,email=Semail,phone=Sphone,gender=Sgender,birth=Sdatebrith,course=Scourse,address=Saddress)
        query1.save()
        messages.success(request,'Student Add Successful') 
       
    return render(request,'Student_Add.html')

def Student_Records(request):
    allposts = Student_Add.objects.all()
    if request.method == 'GET':
        st = request.GET.get('search')
        if st!=None:
            n1=Student_Add.objects.filter(roll_no__icontains=st)
            n2 =Student_Add.objects.filter(name__icontains=st)
            allposts= n1.union(n2)

    return render(request, 'Student_Records.html',{'allposts':allposts })

def Delete_Student(request,id):
    allposts=Student_Add.objects.get(roll_no=id)
    allposts.delete()
    return redirect("/SRecords")


#STUDENT COURSE RECORDS ,ADD

def Student_Course_Records(request):
    q = request.GET.get("search", "")

    books = StudentCourse.objects.filter(
        Q(student__roll_no__icontains=q) |
        Q(course__course_name__icontains=q)
    )
  
    data = StudentCourse.objects.select_related(
        "student",
        "course"
    ).all() 

    return render(
        request,
        "StudentCourse.html",
        {"data": data,"books": books,
        "q": q,}
    )

def Student_Course_Add(request):
    if request.method =="POST":
        studentID = request.POST.get("student_id")
        course_name = request.POST.get("course")
        course_code = request.POST.get("course_code")
        department = request.POST.get("department")
        duration = request.POST.get("duration")
        semster = request.POST.get("sem")
        insructor= request.POST.get("instructor")
        fees = request.POST.get("fees")
        query1 = Student_Course(course_id=studentID,course_name=course_name,course_code=course_code,department=department,duration=duration,semester=semster,Instructor=insructor,fees=fees)
        query1.save()
        messages.success(request,'Student Course Add Successful') 
        
    return render(request,'student_course_add.html')


#STUDENT ATTENDENCE ADD,RECORDS,DELETE

def Student_Attendance_Records(request):
    allposts = Student_Attendence.objects.all()
    if request.method == 'GET':
        st = request.GET.get('search')
        if st!=None:
            n1=Student_Attendence.objects.filter(Roll_no__icontains=st)
            n2 =Student_Attendence.objects.filter(student_name__icontains=st)
            allposts= n1.union(n2)
    
    return render(request, 'Student_Attendance.html',{'allposts':allposts })

def Delete(request,id):
    allposts=Student_Attendence.objects.get(Roll_no=id)
    allposts.delete()
    return redirect("/SAttendanceRecords")


def Student_Attendance_ADD(request):
    if request.method =="POST":
        Sroll_no = request.POST.get("roll")
        Sname = request.POST.get("name")
        Sdate = request.POST.get("date")
        Scourse = request.POST.get("course")
        Sattendance = request.POST.get("address")
        query1 = Student_Attendence(Roll_no=Sroll_no,student_name=Sname,date=Sdate,course=Scourse,attendance=Sattendance)
        query1.save()
        messages.success(request,'Student Attendance Add Successful') 
        return redirect('/SAttendanceRecords')

           
    return render(request,'Student_Attendance_Add.html')

#Register Form
def Register(request):
    if request.method =='POST':
        username = request.POST["username"]
        name = request.POST["name"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        passa = request.POST["passa"]

        try :
            if User.objects.get(username=username):
                messages.error(request,"USERNAME IS TAKEN")
                return redirect('/')
        
        except:
            pass

        try :
            if User.objects.get(email=email):
                messages.success(request,"Email IS TAKEN")
                return redirect('/')
        
        except:
            pass

        myuser = User.objects.create_user(username,email,passa)
        myuser.first_name = name
        myuser.Last_name =lname
        myuser.save()
        messages.success(request,'Register successful') 
        return redirect('/home')
        
    return render(request,'login.html')
    # else:
    #     return HttpResponse('404 Not Found')

# LOGIN FUNCTION
def Login1(request):
    if request.method == 'POST':
        username = request.POST["name"]
        passa = request.POST["passa"]
        user = authenticate(username=username,password=passa)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("/home")

        else:
            messages.error(request," Invalid Credentials, Please Try again")
        
    return render(request,"login.html")
        
# Logout function 
def Logout(request):
    logout(request)
    # messages.success(request, "Successfully Logged Out")
    return redirect("/")
