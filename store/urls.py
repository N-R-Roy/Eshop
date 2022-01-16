from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login


app_name = 'store'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('signup/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
]

