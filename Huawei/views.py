from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
import mimetypes, os
from wsgiref.util import FileWrapper

# generate the file

def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'client.exe'
    # Define the full file path
    filepath = BASE_DIR + '/File/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
def home_page(request):
    return render(request, 'index.html')

def send_message(request):
    messages.success(request, 'Thank You for contacting Huawei, We will get in touch with you soon.')
    return HttpResponseRedirect('/huawei.com')