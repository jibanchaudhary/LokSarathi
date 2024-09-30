from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth.models import User



from .forms import RegisterForm,LoginForm,addQuestionform
from .models import *

### class name from the models.py and the function name in views.py shouln't be same




def index(request):
    return render(request,"index.html",{})


# registration
def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("login")
    context={'RegisterForm':form}
    return render(request,"register.html",context=context)

# Login
def login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("base")
            
    context={'LoginForm':form}
    return render(request,"login.html",context=context)
    

# Logout
@login_required
def logout(request):
    auth.logout(request)
    return redirect("login")

# Syllabus
@login_required
def syllabus_list(request):
    #Fetching the data from the database
    syllabus_name=Syllabus.objects.all()

    return render(request,"syllabus.html",{'syllabus_name':syllabus_name})

@login_required
def base(request):
    return render(request,"base.html")


# This includes the actual quiz logic and the result displaying logic
#Retrieving the data from the db through models.py and passing to the html templates
@login_required
def MCQ(request):
    if request.method=='POST':
        print(request.POST)
        # Getting all the objects from MCQmodel
        questions=MCQmodel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        percent=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.correct_option)
            if q.correct_option==request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10)*100
        print(percent)
        
        context={
            'score':score,
            'wrong':wrong,
            'correct':correct,
            'total':total,
            'time':request.POST.get('timer'),
            'percent':percent,
        }
        return render(request,'mcq_result.html',context=context)
    else:
        questions=MCQmodel.objects.all()
        context={
            'questions':questions
        }
        return render(request,'mcq.html',context=context)
    

    

# This provides the logic for admin to add question
@login_required
def addQuestion(request):
    if request.user.is_staff:
        form=addQuestionform()
        if request.method=='POST':
            form=addQuestionform(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('MCQ')
        context={
            'form':form
        }
        return render(request,'mcq_addqn.html',context=context)
    else:
        return redirect('MCQ')
    

# Retrieve the correct past question pdf from db (in RANK a/c) and pass it to templates
@login_required
def Officer(request):
    prev_qstn = Previousyearqstnmodel.objects.filter(rank='Officer')
    context={
        'prev_qstn':prev_qstn
    }
    return render(request,'officer_level.html',context=context)

@login_required
def Section_officer(request):
    prev_qstn = Previousyearqstnmodel.objects.filter(rank='Section_officer')
    context={
        'prev_qstn': prev_qstn
    }
    return render(request,'section_officer.html',context=context)

#Retrieving the constitution into constitution template
@login_required
def constition(request):
    const_pdf = Constitutionmodel.objects.all()
    context={
        'const_pdf': const_pdf
    }
    return render(request,'constitution.html',context=context)

#Retrieving the books pdf uploaded
@login_required
def books(request):
    books_pdf = Bookmodel.objects.all()
    context={
        'books_pdf':books_pdf
    }
    return render(request,'books.html',context=context)
