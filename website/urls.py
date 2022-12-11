# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from portfolio.views import Error404

urlpatterns = [
    path('yuyutsu/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('favicon.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
]

handler404 = Error404.get_rendered_view()