
from django.urls import path
from . import views

urlpatterns = [
    path('', views.alist),
    path('output', views.output,name="script"),
    path('stop',views.stop,name="stop"),

]
