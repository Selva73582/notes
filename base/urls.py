from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.CustomLogin.as_view(),name="login"),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),\
    path('register/',views.Customregister.as_view(),name="register"),
    path('',views.NoteList.as_view()),
    path('note-list',views.NoteList.as_view(),name='NoteList'),
    path('note-details/<int:pk>/',views.NoteDetail.as_view(),name='NoteDetail'),
    path('note-edit/<int:pk>/',views.NoteEdit.as_view(),name='NoteUpdate'),
    path('note-create/',views.NoteCreate.as_view(),name='NoteCreate'),

]
