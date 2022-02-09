from django.http import HttpResponse, request
from django import template
from django.shortcuts import render
import os
from .models import Image
from dbr import BarcodeReader,BarcodeReaderError
import json
reader = BarcodeReader()
reader.init_license("t0070fQAAAC1k0N1FyFtGgh5xxeziEJcqPfFkdtUmXeO6AH+pELK6QvUYWNxufxVT9XaZxiMsGNvA0k9uzXPkza6oEI3DjSQbCg==") 

# Apply for a trial license: https://www.dynamsoft.com/customer/license/trialLicense?product=dbr&utm_source=github
reader.init_license("LICENSE-KEY")

def index(request):
  return render(request, 'dwt/index.html')

def upload(request):
    out = "No barcode found"
    if request.method == 'POST':
        filePath = handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
        try:
            text_results = reader.decode_file(filePath)
            if text_results != None:
                out = ''
                for text_result in text_results:
                    out += "Barcode Format : " + text_result.barcode_format_string + "\n"
                    out += "Barcode Text : " + text_result.barcode_text + "\n"
                    out += "------------------------------------------------------------"
        except BarcodeReaderError as bre:
            print(bre)
            return HttpResponse(out)


        return HttpResponse(out)
        # image = Image()
        # image.name = request.FILES['RemoteFile'].name
        # image.data = request.FILES['RemoteFile']
        # image.save()
        # return HttpResponse("Successful")

    return HttpResponse(out)

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    filePath = 'upload/' + filename
    with open(filePath, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

        return filePath
