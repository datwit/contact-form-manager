from django.urls import include, path
from manageContact import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('contact/', include('manageContact.urls'))
]
