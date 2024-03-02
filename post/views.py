
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import User, Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate


# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the customized form
    template_name = 'post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  # Redirect to the user's profile page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def posts_by_date(request, date):
    # Retrieve all posts uploaded on the given date
    posts = Post.objects.filter(date_posted__date=date)
    return render(request, 'posts_by_date.html', {'posts': posts, 'date': date})



def user_profile_and_posts(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=user)
    return render(request, 'user_profile_and_posts.html', {'user': user, 'posts': posts})
