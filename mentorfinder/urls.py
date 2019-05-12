from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.CreateMentor.as_view(), name='create'),
    path('find', views.FindMentor.as_view(), name='find'),
    path('detail/<id>', views.MentorDetail.as_view(), name='detail'),
    path('load-mentors', views.load_mentors, name='load-mentors'),
]
