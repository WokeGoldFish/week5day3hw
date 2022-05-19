from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
#import all of your models
from .models import Post

#import all your forms 
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
def index(request):
    posts = Post.objects.all()
    
    context = {'posts':posts}
    return render(request, 'insta/homepage.html', context=context)

def about(request):
    return render(request, 'insta/about.html', context={})

def createPost(request):
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
    else:
        print('get req submitted', request.method)
        
    return render(request, 'insta/createpost.html', context= {'form':form})





def singlePost(request, post_id):
    post = Post.objects.get(id=post_id)
    
    return render(request, 'insta/post.html', context={'p': post})


def updatePost(request, post_id):
    post = PostForm(id = post_id)
    if post.author != request.user:
        # message.warning(request, 'dont be a snek')
        return redirect('home')
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            # messages.success(request, f'updated post {post.id} ty')
            return redirect('post')
    
    context = {
        'p': post,
        'form': form
    }
    return render(request, 'insta/update.html', context = context)
    
    
    
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.author != request.user:
    # message.warning(request, 'dont be a snek')
        return redirect('home')
    
    post.delete()
    # messages.success(request, 'byebye')
    return redirect('home')