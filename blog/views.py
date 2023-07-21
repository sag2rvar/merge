from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, User, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, UserForm, LoginForm, CommentForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm
from .models import Category



def post_list(request,): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

 
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    comment_form = CommentForm() 
    comments = Comment.objects.filter(post=post)
    new_comment= None 
    parent = None
    
    if request.method == 'POST':    
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            try:
                parent = request.POST.get('comment_id')
                parent = Comment.objects.filter(id=parent).last()
            except:
                parent=None

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.parent = parent
            new_comment.save()
        return redirect('blog:post_detail', slug=post.slug)
    else:
        comment_form = CommentForm() 
    return render(request, 'blog/post_detail.html', {'post': post,'form':comment_form, 'comments':comments, 'parent':parent})


def post_new(request,):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            print(post,'pppppppppppppp')
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.tags.set(form.cleaned_data.get('tags'))
            post.save()
            return redirect('blog:post_detail', slug=post.slug) 
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.password = make_password(password) 
            user = form.save()
            login(request, user)
            return redirect('blog:login') 
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})

from django.contrib.auth import login, authenticate  # add to imports

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:post_list')   
            else:
                messages.error(request,"Invalid username or password.")
    else:
        messages.error(request,"Invalid username or password.")
        form = LoginForm()
    return render(request, 'blog/login.html', context={'form': form})
  
@login_required
def profile(request):
    # Retrieve the authenticated user's profile
    user = User.objects.filter(id=request.user.id).last()
    return render(request, 'blog/profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('blog:post_list')

def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'blog/profile_edit.html', {'form': form})  

def posts_by_category(request, id):
    posts = Post.objects.filter(category_id=id)
    return render(request, 'blog/posts.html', {'posts': posts})

def posts_by_tag(request, id):
    posts = Post.objects.filter(tags__id=id)
    return render(request, 'blog/posts.html', {'posts': posts})

def posts_by_author(request, id):
    posts=Post.objects.filter(author_id=id)
    return render(request,'blog/posts.html',{'posts':posts})

  






