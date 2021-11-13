from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('go',views.generate_short,name="generate_short"),
    path("count",views.get_count,name="get_count"),
    path("<str:sh>",views.urlRedirect,name="redirect")
    
]