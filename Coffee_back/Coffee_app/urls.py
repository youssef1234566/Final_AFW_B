from django.urls import path
from Coffee_app.views import *

urlpatterns = [
    path('Sign_Up/', Sign_Up.as_view()),
    path('Sign_In/', Sign_In.as_view()),
    path('profile/', Profile.as_view()),
    path('get_products/', Products.as_view()),

]