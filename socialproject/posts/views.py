from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PostForm
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