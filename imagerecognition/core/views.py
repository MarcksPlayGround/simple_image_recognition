from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from imagerecognition.core.forms import DocumentForm
from imagerecognition.core.imagenet.classify_image import process_image
def home(request):   
    return render(request, 'core/home.html')


def upload_recognize(request):
    if request.method == 'POST' and request.FILES['picforupload']:
        picforupload = request.FILES['picforupload']
        fs = FileSystemStorage()
        filename = fs.save(picforupload.name, picforupload)
        uploaded_file_url = fs.url(filename)
        proci = process_image(filename)
        return render(request, 'core/upload_recognize.html', {
            'uploaded_file_url': uploaded_file_url, 'testvar' : proci
        })
    return render(request, 'core/upload_recognize.html')

