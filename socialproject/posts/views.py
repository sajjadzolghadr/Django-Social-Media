from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm , CommentForm
from .models import Post


# Create your views here.
@login_required(login_url='login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm(data=request.GET)
    return render(request, 'posts/create.html', {'form': form})

@login_required(login_url='login')
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        if post.liked_by.filter(id=request.user.id).exists():
            post.liked_by.remove(request.user)
        else:
            post.liked_by.add(request.user)

    return redirect("index")


@login_required (login_url='login')
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('index')

    return redirect('index')
