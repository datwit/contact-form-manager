from django.urls import path
from manageContact import views

urlpatterns = [
    path('', views.Contact_list),
    path('data/<str:contactID>', views.contact_detail),
]