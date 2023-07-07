from django.urls import path
from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    
    path('register/', views.userFormView.as_view(), name='userform'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('home/', views.home.as_view(), name='main'),
    path("<pk>/", views.detail.as_view(), name="details"),
    # path("blog/<int:pk>/", views.detail.as_view(), name="details"),

]
