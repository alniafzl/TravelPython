from . import views
from django.urls import path
app_name = 'systemapp'

urlpatterns = [
    path('',views.demo,name='demo')
]