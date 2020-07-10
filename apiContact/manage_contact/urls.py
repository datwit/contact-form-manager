from django.urls import path
from manage_contact import views

urlpatterns = [
    path('', views.create_contact),
    path('data/<str:ref_hash>', views.contact_detail),
]