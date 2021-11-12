from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('go',views.generate_short,name="generate_short"),
    path("u/<str:sh>",views.urlRedirect,name="redirect")
]