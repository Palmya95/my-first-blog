from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_latest(request):
	latest_posts_list = Post.objects.all().order_by('-published_date')[:5]
	return render(request, 'blog/post_latest.html', {'latest_posts_list':latest_posts_list})

def category_list(request):
	liste_categories = Category.objects.all()
	return render(request, 'blog/post_latest.html', {'liste_categories':liste_categories})

def category_posts(request):
	posts_categorie1 = Post.objects.filter(category=1)
	return render(request, 'blog/posts_categorie1.html', {'posts_categorie1':posts_categorie1})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})