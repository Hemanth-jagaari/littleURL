from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('go',views.generate_short,name="generate_short"),
    path("<str:sh>",views.urlRedirect,name="redirect"),
    path("count",views.get_count,name="get_count")
]