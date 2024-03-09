from django.urls import path
from . import views

app_name = 'user_home'
urlpatterns = [
    path('', views.home, name='home'),
    path('awareness_and_education/', views.awareness_and_education, name = 'awareness_and_education'),
    path('support_helpline_section/', views.support_helpline_section, name = 'support_helpline_section')
]
