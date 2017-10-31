from django.shortcuts import render_to_response
from .models import BlogPost

archive = lambda req: render_to_response('archive.html', {'posts': BlogPost.objects.all()[:5]})