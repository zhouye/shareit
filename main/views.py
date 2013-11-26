from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

from main.models import Document
from main.forms import DocumentForm

def index(request):
    documents = Document.objects.all()
    return render_to_response(
        'main/index.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )

@login_required
def file(request,file_id):
    document = Document.objects.get(id=int(file_id))
    if request.method == 'GET':
        if request.GET.get('add') == '1':
            
            document.score = document.score + 1
            document.save()
    return render_to_response(
        'main/file.html',
        {'document': document},
        context_instance=RequestContext(request)
    )       
@login_required
def upload(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():   
            newdoc = Document(title = request.POST['title'], file = request.FILES['docfile'], score=0)
            newdoc.save()
            return HttpResponseRedirect('index')
    else:
        form = DocumentForm()
    return render_to_response(
        'main/upload.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
