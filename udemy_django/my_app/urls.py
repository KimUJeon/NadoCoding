from django.urls import path
from . import views

# URL 네임 지정에 사용
app_name = "my_app"

urlpatterns = [
    path('', views.example_view, name="example"),
    path('variable/', views.variable_view, name="variable"),
]