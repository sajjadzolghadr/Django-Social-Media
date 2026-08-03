from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .froms import UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile
from posts.models import Post,SavedPost
# Create your views here.
@login_required(login_url='login')
def index(request):
    posts = Post.objects.select_related('user').order_by('-created')
    saved_post_ids = []
    if request.user.is_authenticated:
        saved_post_ids = SavedPost.objects.filter(
            user=request.user
        ).values_list('post_id', flat=True)
    return render(request, "users/index.html", {"posts": posts, "saved_post_ids": list(saved_post_ids)})
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})

@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})
