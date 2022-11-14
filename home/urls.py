from home import views
from django.urls import path
from home.views import personal,education,experience,project,social,add_info
urlpatterns=[
    path('',views.home,name='home'),
    path('personal',views.personal,name='personal'),
    path('education',views.education,name='education'),
    path('experience',views.experience,name='experience'),
    path('project',views.project,name='project'),
    path('social',views.social,name='social'),
    path('add_info',views.add_info,name='add_info'),
    path('certification',views.certification,name='certification'),
]