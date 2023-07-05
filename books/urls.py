# from django.urls import path
# from . import views
# urlpatterns = [
#     path('books/', views.index, name="index"),
    
# ]


from django.urls import path
from . import views

urlpatterns = [
    ## This will serve as the link to the home page which is the index
    path("", views.index, name="index"),  
    # Other URL patterns for your project...
    # books/1, where this means the id of different sections or book collections. Note thst the 1 can be another number
    # path("")
]