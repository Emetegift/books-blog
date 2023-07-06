from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View # This will work for the View in the form class 
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

class userFormView(View):
    form_class=UserForm
    template_name = 'books/register.html'

    def get(self,request):
        form = self.form_class(None)
        return render (request, self.template_name,{'form':form})
    
    
    
    def post(self,request):
        form = self.form_class(request.POST)

        ## To register and authenticate a user
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            newuser=authenticate(username=username, password=password)

            if newuser is not None:
                if newuser.is_active:
                    login(request,newuser)
                    return redirect("/books")
                
        ## If the user is not authenticated, that is he does not exist, or fill in wrong details, give them another form to fill
        return render (request, self.template_name,{'form':form})