from django.urls import path
from . import views

urlpatterns = [
    # ticket
    path('', views.TicketCreateView, name='create-ticket'),
    path('send-message/', views.TicketSendMessageView.as_view(), name='send-message'),
]
