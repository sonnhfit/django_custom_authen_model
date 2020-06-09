from django.urls import path
from .views import FormView

urlpatterns = [
    path('abd/', FormView.as_view(), name='form_url1')

]
