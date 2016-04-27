from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import CreateView
from .forms import PostForm, CommentForm

def index(request):
    return render(request, 'blog/index.html')
# Create your views here.

def post_list(request):
    post_list = Post.objects.all()[:10]
    return render(request, 'blog/index.html', {
        'post_list': post_list,
        })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post':post,
        })


def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
           # return redirect('blog:post_detail', post.pk)

    else :
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form':form,
        })  

#upgrade version. overwirte
post_new = CreateView.as_view(model=Post, form_class=PostForm)






def comment_new(request, post_pk):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #innerside, do not run model instance 'save' function
            comment.post = Post.objects.get(pk=post_pk) #add post _ id
            comment.save()
            return redirect('blog:post_detail', comment.post.pk)
    else :
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form':form,
        })
