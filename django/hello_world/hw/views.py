# Create your views here.
from django.shortcuts import HttpResponse
from django.template import Context, loader
from datetime import datetime


def hello_view(request):
    return HttpResponse(
        """
        <html>
        <head>
        <title>Hello world</title>
        </head>
        <body>
        <h2>Hello world</h2>
        </body>
        </html>
        """
    )


def better_hello(request):
    t = loader.get_template("hw/betterhello.html")
    c = Context({'current_time': datetime.now()})
    return HttpResponse(t.render(c))
