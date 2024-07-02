from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Doctor, Patient, Appointment
# from .forms import AppointmentForm


from django.shortcuts import render
from .models import Doctor, Patient, Appointment

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def Appointment(request):
    return render(request, 'appointment.html')

def Contact(request):
    return render(request, 'contact.html')

def Feature(request):
    return render(request, 'feature.html')

def Service(request):
    return render(request, 'service.html')

def Team(request):
    return render(request, 'team.html')

def Testimonial(request):
    return render(request, 'testimonial.html')

def error(request):
    return render(request, '404.html')


# class DoctorDetailView(DetailView):
#     model = Doctor
#     template_name = 'appointment.html'
#     context_object_name = 'doctor'
#
# class PatientListView(ListView):
#     model = Patient
#     template_name = 'contact.html'
#     context_object_name = 'patients'
#
# class PatientDetailView(DetailView):
#     model = Patient
#     template_name = 'feature.html'
#     context_object_name = 'patient'
#
# # def appointment_create(request):
# #     if request.method == 'POST':
# #         form = AppointmentForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('appointment_list')
# #     else:
# #         form = AppointmentForm()
# #     return render(request, 'clinic/appointment_form.html', {'form': form})
#
# class AppointmentListView(ListView):
#     model = Appointment
#     template_name = 'service.html'
#     context_object_name = 'appointments'