from django.shortcuts import render
from.forms import Loginform,PatientForm
from.models import Login,Patient

# Create your views here.
def home(request):
    return render(request,'home.html')


#patient registration

def patientregisteration(request):
    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=PatientForm()
    return render(request, 'patientRegisteration.html')


#doctor registration

def doctorregistration(request):
    return render(request,'doctorregistration.html')



def login(request):
    
    return render(request,'login.html')



def appointment(requet):
    return render(requet,'appointment.html')



def patientmodule(requet):
    return render(requet,'patientmodule.html')
