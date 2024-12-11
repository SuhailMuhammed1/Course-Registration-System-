from django.urls import path
from course_app import views

urlpatterns = [  # urls for the pages
    path('', views.course_list),
    path('register/', views.register_course),
    path('add_course/', views.add_course),
]