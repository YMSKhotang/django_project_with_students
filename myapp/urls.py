
from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.base, name='base'),
    path('posts/',views.post, name='post'),
    path('post/<int:id>',views.detail, name='detail'),
] 