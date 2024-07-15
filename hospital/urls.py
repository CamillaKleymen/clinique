from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from clinic import views
from clinic.views import home, about, Appointment, Contact, Feature, Service, Team, Testimonial, error, mainpage, \
    Cardiology, Ocolus, Neuro, Trauma, Stoma, Diagnos, feedback, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index.html', mainpage, name='main page'),
    path('about.html', about, name='about'),
    path('appointment.html', Appointment, name='appointment'),
    path('contact.html', Contact, name='contact'),
    path('feature.html', Feature, name='feature'),
    path('service.html', Service, name='service'),
    path('team.html', Team, name='team'),
    path('testimonial.html', Testimonial, name='testimonial'),
    path('404.html', error, name='error'),
    path('cardiology.html', Cardiology, name='cardiology'),
    path('ocolus.html', Ocolus, name='ocolus'),
    path('trauma.html', Trauma, name='trauma'),
    path('stoma.html', Stoma, name='stoma'),
    path('diagnos.html', Diagnos, name='diagnos'),
    path('neuro.html', Neuro, name='neuro'),
    path('appointment/', views.appointment, name='appointment'),
    path('testimonial/', feedback, name='testimonial'),
    path('contact/', contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)