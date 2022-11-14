from accounts import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signUp,name='signup'),
    path('signin',views.signIn,name='signin'),
    path('signout',views.signOut,name='signout'),
]