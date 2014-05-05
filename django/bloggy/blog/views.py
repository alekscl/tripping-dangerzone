# Create your views here.
from django.http import HttpResponse
from blog.models import Post
from django.template import Context, loader


def index(request):
    latest_posts = Post.objects.all()
    t = loader.get_template('blog/index.html')
    c = Context({'lastes_posts': latest_posts})
    return HttpResponse(t.render(c))
