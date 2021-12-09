from django.shortcuts import render
# Create your views here.
from .models import File
from django.contrib import messages
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

def index(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['uploadedFile']
        title = request.POST["title"]
        
        try:
            fs = File(title=title, file=uploaded_file)
            fs.save()
            messages.success(request, 'Form submission successful')
        except:
            messages.error(request, 'Upload Error.')

    return render(request, 'index.html')

def details(request):
    context = {"files": []}
    try:
        files = File.objects.all()
        # context['files'] = files
        for i in range(len(files)):
                    file = {}
                    file_url = str(files[i].file)
                    file["url"] = gd_storage.url(file_url)
                    file["title"] = files[i].title.capitalize()
                    file["pub_date"] = files[i].pub_date.strftime('%Y - %m -  %d')
                    context['files'].append(file)
    except:
        context['files'] = []
    return render(request, 'details.html', context)