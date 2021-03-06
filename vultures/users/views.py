from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View, ListView, DetailView
from .forms import CustomUserCreationForm, CreateForm

from users.models import Person, FoodPost, FoodComment, Map

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class LoginView(TemplateView, View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                messages.success(request, "You are now logged in!")
            else:
                messages.warning(request, "The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            messages.warning(request, "The username and password were incorrect.")

        return redirect(request.POST.get('next', 'home'))


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('home')

        logout(request)
        messages.success(request, "You are now logged out!")
        return redirect('home')


class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.warning(request, "You are already logged in!")
            return redirect('home')
        return self.render_to_response({'form': CustomUserCreationForm()})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You can now login!")
            return redirect('home')
        else:
            return self.render_to_response({'form': form})


class MembersView(ListView):
    model = Person
    template_name = 'users/members_only.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            messages.warning(request, "Please login first")
            return redirect('home')
        else:
            model = Person
            object_list = Person.objects.all()
            context = {'person_list' : object_list}
            return render(request, 'users/members_only.html', context)
    #queryset = Person.objects.all()
    #def get(self, request, *args, **kwargs):
     #   return self.render_to_response({})

class ProfileDetailView(DetailView):
    template_name = 'users/profile.html'
    model = Person

class PostView(TemplateView):
    template_name = 'users/post.html'

class FeedView(ListView):
    template_name = 'users/feed.html'
    model = FoodPost

class FeedDetailView(DetailView):
    template_name = 'users/post_details.html'
    model = FoodPost

class CommentListView(ListView):
    template_name = 'users/comment_list.html'
    model = FoodComment

class CommentDetailView(DetailView):
    template_name = 'users/comment_details.html'
    model = FoodComment

class CreatePost(CreateView):
    model = FoodPost
    # fields = ['location', 'postDate', 'postInfo']
    form_class = CreateForm

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.postUser = self.request.user
        return super(CreatePost, self).form_valid(form)
    
class UpdatePost(UpdateView):
    model = FoodPost
    fields = ['location','foodType', 'roomNum', 'postDate', 'postInfo']

class DeletePost(DeleteView):
    model = FoodPost
    success_url = reverse_lazy('feed')
    
class MapView(ListView):
    template_name = 'users/map.html'
    model = Map