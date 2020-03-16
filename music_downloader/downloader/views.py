from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
import os

# Create your views here.

def handle_uploaded_file(f):
    '''
    writes the file to the server
    '''
    with open(settings.MEDIA_ROOT + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            handle_uploaded_file(file)
            return HttpResponse(f'File {file.name} Uploaded')
        else:
            raise Http404('File upload failed')
    else:
        return HttpResponseNotAllowed(['POST',])


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/force-download")
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    raise Http404
