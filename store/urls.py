from django.urls import path
from .views import *
urlpatterns=[
    path('',Index.as_view(),name='index'),
    path('signup/',sign_up,name="signup"),
    #path('log/',Login,name="loginusr"),
    path('log/',Login,name="loginusr"),
    path('lgout/',Logout,name="logout1"),
    path('cart/',Cart.as_view(),name="cart"),
    path('check-out/',CheckOut.as_view(),name="checkout"),
    path('order/',Order_Show.as_view(),name="order"),
]