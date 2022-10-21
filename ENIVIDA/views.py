from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.Press_Release import Press
from .models.tender import Tender
from .models.Bidder import User
from .models.filetender import etender
from django.contrib.auth.hashers import make_password, check_password

tEN = Tender.get_all_Tender()
error = None
# Create your views here.
def index(request):
    PR=Press.get_all_Press();

    return render(request,'index.html' ,{'Press':PR , 'Tendr':tEN}  )

def Uindex(request):
    PR=Press.get_all_Press();

    return render(request,'U.index.html' ,{'Press':PR, 'Tendr':tEN}  )

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        user= User.get_user_by_email(Email)
        if user:
            flag = check_password(Password, user.Password)
            if flag:
                return redirect('verifyotp')
            else:
                error = 'Invalid Password! Enter correct password.*'
                return render(request, 'login.html', {'error':error})

        else:
            error = 'Invalid Email! Enter correct email.*'
        print(error)
        return render(request, 'login.html', {'error':error})

    elif request.method == 'put':
        return render(request, 'U.base.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Bidder_Mobile = request.POST.get('Bidder_Mobile')
        Password = request.POST.get('Password')
        Company_Name = request.POST.get('Company_Name')
        Registration_Number = request.POST.get('Registration_Number')
        Registered_Address = request.POST.get('Registered_Address')
        Partners_or_Directors = request.POST.get('Partners_or_Directors')
        City = request.POST.get('City')
        State = request.POST.get('State')
        Postal_Code = request.POST.get('Postal_Code')
        PAN_TAN_Number = request.POST.get('PAN_TAN_Number')
        Estd_Year = request.POST.get('Estd_Year')
        Nature_of_Business = request.POST.get('Nature_of_Business')
        Legel_Status = request.POST.get('Legel_Status')

        emailerror = None

        x= User.isExists(Email)
        if (x):
            emailerror = 'This email is already Registered, use another email.*'
            print(emailerror)

        if not emailerror:
            user = User(
                Name=Name,
                Email = Email,
                Bidder_Mobile=Bidder_Mobile,
                Password= make_password(Password),
                Company_Name=Company_Name,
                Registration_Number=Registration_Number,
                Registered_Address=Registered_Address,
                Partners_or_Directors=Partners_or_Directors,
                City=City,
                State=State,
                Postal_Code=Postal_Code,
                PAN_TAN_Number=PAN_TAN_Number,
                Estd_Year=Estd_Year,
                Nature_of_Business=Nature_of_Business,
                Legel_Status=Legel_Status

            )

            print("Running")
            user.save()
            return redirect('login')

        else:
            return render(request, 'signup.html', {'emailerror': emailerror})


def filetender(request):
    if request.method == 'GET':
        return render(request,'filetender.html')
    elif request.method == 'POST':
        Biddername = request.POST.get('Biddername')
        Tender_ID = request.POST.get('Tender_ID')
        Tender_Type = request.POST.get('Tender_Type')
        Tender_Category = request.POST.get('Tender_Category')
        Total_Projects_Worked = request.POST.get('Total_Projects_Worked')
        Total_Success_Projects = request.POST.get('Total_Success_Projects')
        Organization_size = request.POST.get('Organization_size')
        Organization_established_Year = request.POST.get('Organization_established_Year')
        Value_of_Last_Project = request.POST.get('Value_of_Last_Project')
        Proposed_Cost_of_Project = request.POST.get('Proposed_Cost_of_Project')

        eten = etender(
            Biddername = Biddername,
            Tender_ID = Tender_ID,
            Tender_Type = Tender_Type,
            Tender_Category = Tender_Category,
            Total_Projects_Worked = Total_Projects_Worked,
            Total_Success_Projects = Total_Success_Projects,
            Organization_size = Organization_size,
            Organization_established_Year = Organization_established_Year,
            Value_of_Last_Project = Value_of_Last_Project,
            Proposed_Cost_of_Project = Proposed_Cost_of_Project
            )

        eten.save()

        return HttpResponse('Tender Filed')


def activetender(request):
    return render(request, 'activetender.html', {'Tender':tEN})

def cancelledtender(request):
    return render(request, 'cancelledtender.html')

def recruitment(request):
    return render(request, 'recruitment.html')

def circular(request):
    return render(request, 'circular.html')

def events(request):
    return render(request, 'events.html')

def contactus(request):
    return render(request, 'contactus.html')

def media(request):
    return render(request, 'media.html')

'''
l1=etender.objects.all().order_by('Proposed_Cost_of_Project').values()
print(l1)
print('\n\nQCBS\n\n')

QCBS=etender.objects.all().order_by('Organization_established_Year','Proposed_Cost_of_Project','-Total_Projects_Worked','-Total_Success_Projects','-Value_of_Last_Project').values()
print(QCBS)

'''


