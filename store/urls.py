from django.urls import path
from .views.index import Index
from .views.signup import Signup
from .views.login import Login
from .views.logout import logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.order import OrderView
from .views.search import Search
from .views.detail import Detail
from store.views.about import about
from store.middlewares.auth import auth_middleware


app_name = 'store'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('signup/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('cart/', Cart.as_view(), name="cart"),
    path('logout/', logout, name="logout"),
    path('check-out/', auth_middleware(CheckOut.as_view()), name="checkout"),
    path('order/', auth_middleware(OrderView.as_view()), name="order"),
    # path('order/', OrderView.as_view(), name="order"),
    path('search-product/', Search.as_view(), name="search-product"),
    path('about/', about, name='about'),
    path('detail/<int:p_id>/', Detail.as_view(), name='detail'),
]

