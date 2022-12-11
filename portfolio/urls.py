# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'portfolio'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('projects', views.ProjectListView.as_view(), name='project-list'),
    path(
        'project/<slug:slug>/', views.ProjectDetailView.as_view(),
        name='project-detail'),
    path('contact/', views.contact_view, name='contact'),
    path(
        'experience/', views.ExperienceListView.as_view(),
        name='experience-list'),
    path('gist/', views.NoteListView.as_view(), name='note-list'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
