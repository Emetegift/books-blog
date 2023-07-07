from django.urls import path
# from .views import RegisterPage
from . import views

urlpatterns = [
    ## This will serve as the link to the home page which is the index
    
    path("", views.index.as_view(), name="index"),  
    # Other URL patterns for your project...
    # books/1, where this means the id of different sections or book collections. Note thst the 1 can be another number
    path('register/', views.userFormView.as_view(), name='userform'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path("<pk>/", views.detail.as_view(), name="details"),
    
    
]
