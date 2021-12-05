from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import CreatePostForm
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
# Create your views here.

def BlogHome(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def Login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(username=user_name, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {user_name}')
            return redirect('dashboard')
        else:
            return HttpResponse('There was an error logging in')
    return render(request, 'blog/login.html', {})

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            return HttpResponse('Wrong password!')
        else:
            pass

        user = User.objects.create_user(username, email, pass2)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, f'Account successfully created for {fname}. Login now')
        return redirect('dashboard-login')

    return render(request, 'blog/register.html', {})

def LogoutAdmin(request):
    logout(request)
    return redirect('dashboard-login')

@login_required
def AdminPage(request):
    return render(request, 'blog/admin.html', {})

def Article(request, id):
    # data = Post.objects.get(id = id)
    # context = {
    #     'data': data
    # }
    # return render(request, 'blog/article_detail.html', context)
    pass

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Post.objects.all()

    def get_object(self):
        id_  = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)

@login_required
def CreatePost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post was successfully published!!!')

        else:
            form = CreatePostForm
            

    form = CreatePostForm
    return render(request, 'blog/post create.html', {'form': form})