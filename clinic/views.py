from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Doctor, Patient, Appointment
# from .forms import AppointmentForm
from django.shortcuts import render, redirect
from django.contrib import messages
from telebot import TeleBot

from django.shortcuts import render
from .models import Doctor, Patient, Appointment

def home(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def Appointment(request):
    return render(request, 'appointment.html')

def Contact(request):
    return render(request, 'contact.html')

def Feature(request):
    return render(request, 'feature.html')
def Cardiology(request):
    return render(request, 'cardiology.html')

def Ocolus(request):
    return render(request, 'ocolus.html')

def Stoma(request):
    return render(request, 'stoma.html')

def Diagnos(request):
    return render(request, 'diagnos.html')

def Trauma(request):
    return render(request, 'trauma.html')

def Neuro(request):
    return render(request, 'neuro.html')



def Service(request):
    return render(request, 'service.html')

def Team(request):
    return render(request, 'team.html')

def Testimonial(request):
    return render(request, 'testimonial.html')

def error(request):
    return render(request, '404.html')


bot = TeleBot('7004032681:AAHroW2_ZA01ingIwYEyRmH7gM0Oo558Jl8')

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        problem = request.POST.get('problem')

        # Формируем текст сообщения
        message_text = f"""
            Новая запись на прием!
            Имя: {name}
            Email: {email}
            Телефон: {phone}
            Выбранный врач: {doctor}
            Дата: {date}
            Время: {time}
            Описание проблемы: {problem}
            """

        # Отправляем сообщение в Telegram
        bot.send_message(-1002242936359, message_text)

        # Добавляем сообщение об успешной записи
        messages.success(request, 'Вы успешно записались на прием. Мы свяжемся с вами для подтверждения.')

        # Перенаправляем на главную страницу
        return redirect('/')
    else:
        return render(request, 'appointment.html')


def feedback(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Формируем текст сообщения
        feedback_message = f"""
            Новый отзыв!
            Email: {email}
            Сообщение: {message}
        """

        # Отправляем сообщение в Telegram
        bot.send_message(-1002242936359, feedback_message)  # Замените на ваш chat_id

        # Добавляем сообщение об успешной отправке
        messages.success(request, 'Ваш отзыв успешно отправлен. Спасибо за ваш вклад!')

        # Перенаправляем на главную страницу или другую страницу
        return redirect('/')
    else:
        return render(request, 'testimonial.html')




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Формируем текст сообщения
        feedback_message = f"""
            Новый отзыв!
            Имя: {name}
            Email: {email}
            Тема: {subject}
            Сообщение: {message}
        """

        # Отправляем сообщение в Telegram
        bot.send_message(-1002242936359, feedback_message)  # Замените на ваш chat_id

        # Добавляем сообщение об успешной отправке
        messages.success(request, 'Ваш отзыв успешно отправлен. Спасибо за ваш вклад!')

        # Перенаправляем на главную страницу или другую страницу
        return redirect('/')
    else:
        return render(request, 'contact.html')


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