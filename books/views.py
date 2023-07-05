from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# from .models import Task 
# Create your views here.
# def index(request):
#     all_collection = Collection.objects.all() 
#     context = {
#         "all_collections" : all_collection
#     }
#     return render(request, "books//bookstemplate.html", context)

## To write a neater code using the generic function

class index(generic.ListView):
    template_name='books/books.html'

    def get_queryset(self):
        
        return Collection.objects.all()

# def details(request, books_id):
#     citem = Collection.objects.get(pk=books_id)
#     pitems = Piece.objects.filter(collection=citem)
#     context = {
#         "pitems" : pitems
#     }
#     return render(request, "books\\detailstemplate.html", context)


## To write a neater code using the generic function


class detail (generic.DetailView): # DetailView always accept one parameter
    model = Collection
    template_name='books/detailstemplate.html'

class RegisterPage(FormView):
    template_name = 'books/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')  
    
    # To redirect the user once the registration form is submitted
    def  form_valid(self, form):
        user = form.save()
        if user is not None: # This means if the user was successfully created
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)  

    def get(self,*args,**kwargs): # keyword arguments
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

class details(generic.DetailView):
    model = Collection
    template_name = 'books/detailstemplate.html'