from django.urls  import path
from . import views
urlpatterns=[
        path('',views.MyView),
        path('json',views.MyJson),
        ]
