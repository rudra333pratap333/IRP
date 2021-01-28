from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('<int:req_id>/',views.feedback, name='feedback'),
    path("search_candidate/", views.search_candidate, name = 'search_candidate'),
    path('test/', views.test, name = 'test_name'),
]
