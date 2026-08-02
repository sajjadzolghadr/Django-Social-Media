from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
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


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        if post.liked_by.filter(id=request.user.id).exists():
            post.liked_by.remove(request.user)
        else:
            post.liked_by.add(request.user)

    return redirect("index")
