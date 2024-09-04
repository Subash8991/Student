from django.http import HttpResponse
from django.shortcuts import render, redirect
from Myapp.models import User
from Myapp.form import User_form

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        PhoneNumber=request.POST['PhoneNumber']
        Dateofjoin=request.POST['Dateofjoin']
        obj=User()
        obj.Name=name
        obj.Age=age
        obj.Email=email
        obj.Phonenumber=PhoneNumber
        obj.Dateofjoin=Dateofjoin
        obj.save()
       
    return render(request, 'Home.html')

def add(request):
    a = User_form()
    
    # if request.method=='POST':
    #     name=request.POST['name']
    #     age=request.POSt['age']
    #     email=request.POST['email']
    #     phone=request.POST['phone']
    #     doj=request.POST['doj']
    #     obj=User(Name=name,Age=age,Email=email,PhoneNumber=phone,DateofJoin=doj)
        # name =request.POST['name']
        # age=request.POST['age']
        # Email=request.POST['email']
        # PhoneNumber=request.POST['Phone']
        # Dateofjoin=request.POST['doj']
        # obj=User()
        # obj.Name=name
        # obj.Age=age
        # obj.Email=Email
        # obj.Phonenumber=PhoneNumber
        # obj.Dateofjoin=Dateofjoin
        # obj=User(Name=name,Age=age,Email=Email,PhoneNumber=PhoneNumber,Dateofjoin=Dateofjoin)
      #  obj.save()
        #return render(request,'success.html')
    return render(request,'Addstudent.html')
 
def addData(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phonenumber=request.POST['phone']
        dateofjoin=request.POST['doj']
        obj=User()
        # obj.Name=name
        # obj.Age=age
        # obj.Email=email
        # obj.Phonenumber=PhoneNumber
        # obj.Dateofjoin=Dateofjoin
        obj=User(Name=name,Age=age,Email=email,PhoneNumber=phonenumber,Dateofjoin=dateofjoin)
        obj.save()
        # mydata=User.objects.all()
        return render(request, 'success.html')

def details(request):
    a = User.objects.all()
    return render(request,'AllStudentDetails10.html',{'b':a})

def fetch(request):
    # name=request.POST['name']
    # b=User.objects.filter(name=a)
    
    return render(request,'Name_Add.html')
    # return render(request,'Name_Add.html',{'a':b})

def fetchname(request):
    a=request.POST['name']
    b=User.objects.filter(Name=a)
    print(b)
    return render(request,'StudentDetails.html',{'b':b})

def update(request):
    return render(request,'Update.html')

def home(request):
    #return redirect(url_for('home'))
    return redirect('index')

def button1(request):
    return redirect('add')

def home1(request):
    #return redirect(url_for('home'))
    return redirect('index')

   
def submi(request):
    return render(request,'success.html')

def updateData(request,u_id):
    mydata=User.objects.filter(id=u_id)
    return render(request,'updatevalue.html',{'b':mydata})

def update_form(request):
    mydata=request.POST['u_id']
    b=request.POST['name']
    c = request.POST['age']
    d = request.POST['email']
    e=request.POST['phone']
    f=request.POST['doj']
    g=User.objects.filter(id=mydata)
    g.update(Name=b,Age=c,Email=d,PhoneNumber=e,Dateofjoin=f)
    return redirect(details)

def deleteData(request,id):
     mydata=User.objects.get(id=id)
     mydata.delete()
     return redirect('details')

def view(request,u_id):
     mydata=User.objects.filter(id=u_id)
     return render(request,'view.html',{'b':mydata})

    



