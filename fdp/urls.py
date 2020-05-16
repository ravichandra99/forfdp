from django.urls import path
from fdp import views

app_name = 'fdp'

urlpatterns = [
    path('', views.index, name='index'),
    # chat API
    path('send/', views.message_sent, name='send'),
    path('history/', views.history, name='history'),

]
