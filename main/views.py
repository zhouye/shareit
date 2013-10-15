from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from main.models import Document
from main.forms import DocumentForm

def index(request):
    template = loader.get_template('main/index.html')
    documents = Document.objects.all()
    return render_to_response(
        'main/index.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )

def upload(request):
    template = loader.get_template('main/upload.html')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(title = request.POST['title'], file = request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect('index')
    else:
        form = DocumentForm() # A empty, unbound form
    return render_to_response(
        'main/upload.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
