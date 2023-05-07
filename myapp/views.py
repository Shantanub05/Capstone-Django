import gzip
from django.http import StreamingHttpResponse
from django.shortcuts import render
from camera import *
from myapp.camera import VideoCamera, gen


def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad!
        pass

def index(request, *args, **kwargs):
    return render(request, 'index.html')