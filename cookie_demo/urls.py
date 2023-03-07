from django.urls import path
from . import views

urlpatterns = [
    path('set', views.setcookie, name='set'),
    path('get', views.getcookie, name='get'),
    path('del', views.delcookie, name='del'),
    path('view1', views.my_view, name='view1'),
    path('view2', views.my_other_view, name='view2'),
    path('view3', views.my_newview, name='view3'),
]
