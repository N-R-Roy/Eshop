from django.urls import path
from .views.home import index
from .views.signup import Signup
from .views.login import Login


app_name = 'store'

urlpatterns = [
    path('', index, name="index"),
    path('signup/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
]

