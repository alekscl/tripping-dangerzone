# Create your views here.
from django.http import HttpResponse
from django.shortcuts import RequestContext, render_to_response
from django.shortcuts import get_object_or_404
from blog.models import Post
from django.template import Context, loader
from blog.forms import PostForm


def index(request):
    latest_posts = Post.objects.all()
    t = loader.get_template('blog/index.html')
    c = Context({'latest_posts': latest_posts})
    return HttpResponse(t.render(c))


def blog_entry(request, year, id):
    try:
        post = get_object_or_404(Post, id=id)
        t = loader.get_template('blog/blog_entry.html')
        c = Context({'post': post})
        return HttpResponse(t.render(c))
    except Post.DoesNotExist:
        return index(request)


def new_post(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            form.errors
    else:
        form = PostForm()
    return render_to_response("blog/newentry.html", {'form': form}, context)
