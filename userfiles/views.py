from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from userfiles.models import File
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.conf import  settings
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')
def uploadFiles(request):
    files = request.FILES.getlist('filesList')
    if len(files) == 0:
        return JsonResponse({'status' : 0, 'message' : 'file required'})
    for file in files:
        fileObject = File()
        fileObject.user_id = request.session['userId']
        fileObject.name = file.name
        handleFileUploading(file)
        fileObject.save()
    return JsonResponse({'status' : 1, 'message' : 'Files uploaded'})


def handleFileUploading(f):
    file_name = default_storage.save('uploads/' + f.name, f)

def myfiles(request):
    files = File.objects.filter(user_id=request.session['userId'])
    for file in files:
        file.url = default_storage.url('uploads/' + file.name)

    context = {
        'files': files
    }
    return render(request, 'my-files.html', context)

def deletefile(request, id):
    file = File.objects.get(id=id)
    file.delete()
    return redirect('myfiles')