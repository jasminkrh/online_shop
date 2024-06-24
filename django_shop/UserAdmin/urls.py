from django.urls import path
from . import views

from UserAdmin.views import SignUpView

urlpatterns = [
    path('show_myusers/', views.MyUserListView.as_view(), name='myuser-list'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.MySignUpView.as_view(), name='signup'),
]