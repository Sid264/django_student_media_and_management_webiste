import profile
from django.shortcuts import render, redirect, get_object_or_404
from home.forms import form1
from django.contrib.auth.models import User
from .models import UserProfile
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')


class Register(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'register.html')
    
    def post(self,request):
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName")
            sex = request.POST.get("sex")
            institute = request.POST.get("institute")
            course = request.POST.get("course")
            subject = request.POST.get("subject")
            startingDate = request.POST.get("startingDate")
            endingDate = request.POST.get("endingDate")
            email = request.POST.get("email")
            password1 = request.POST.get("password")
            password2 = request.POST.get("cpassword")
            address1 = request.POST.get("address1")
            city = request.POST.get("city")
            state = request.POST.get("state")
            zip = request.POST.get("zip")
                        
            
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return render(request, 'form1.html', {'message':"Password doesn't match"})
        
           
            userOb = User.objects.create_user(
                username=email,
                password=password1,
                email=email,
                first_name=firstName,
                last_name=lastName
            )
            userOb.save()
             
            
            if (userOb != None):
                profileOb = UserProfile.objects.create(
                    sex=sex,
                    institute=institute, 
                    course=course,
                    subject=subject,
                    startingDate=startingDate,
                    endingDate=endingDate,
                    fullAddress=address1,
                    city=city,
                    state=state,
                    zip=zip,
                    user=userOb
                )
                profileOb.save()
            return render(request, 'login.html',{'message':"Registration done Successfully"})



class Login(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username=request.POST.get("username")
        pwd=request.POST.get("password")
        auth = authenticate(username=username,password=pwd)
        # print(auth)
        if(auth):
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'message':"Wrong Creditionals. The detail that you've entered is incorrect."})

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def form1_view(request):
    form = form1()
    return render(request, 'form1.html', {'form': form})


def dashboard(request):
    profiles = UserProfile.objects.all()
    return render(request, 'dashboard.html', {'profiles':profiles})


def profileDetails(request, pk):
    Profile = get_object_or_404(UserProfile, pk=pk)
    context = {'profile': profile}
    return render(request, 'profileDetails.html', context)

class SendEmailView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get("phone")
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        subject = 'Appointment Booking'
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}"
        from_email = 'dasananda607@gmail.com'
        to_email = ['sid.studentmedia@example.com'
                    'sudippramanik34150@gmail.com'
                    ]
        
        send_mail(subject, message, from_email, [to_email])
        
        return render(request, 'contact.html', {'message':"Appoitment requested successfully."})
    

def logout(request):
    return redirect('home')