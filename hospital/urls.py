from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from clinic import views
from clinic.views import home, about, Appointment, Contact, Feature, Service, Team, Testimonial, error, mainpage

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

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)