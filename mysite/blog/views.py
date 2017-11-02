from django.shortcuts import render_to_response
from .models import BlogPost
from datetime import datetime
from django.http import HttpResponseRedirect
from django.template import RequestContext

archive = lambda req: render_to_response('archive.html', {'posts': BlogPost.objects.all()[:5]}, RequestContext(req))

def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title = request.POST.get('title'),
            body = request.POST.get('body'),
            timestamp = datetime.now(),
        ).save()
    return HttpResponseRedirect('/blog/')

