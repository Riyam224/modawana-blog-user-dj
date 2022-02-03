from django.shortcuts import render , get_object_or_404

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request , 'blog/home.html', context)

def about(request):
    context = {
        'title': 'about'
    }

    return render(request, 'blog/about.html', context)

def post_detail(request , pk):
    post = get_object_or_404(Post , pk=pk)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            #  todo ! connect comment with post
    
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()

    context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request , 'blog/detail.html', context)