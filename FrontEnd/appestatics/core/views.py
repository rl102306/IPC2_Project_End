from django.shortcuts import render , HttpResponse

from django.core.files.storage import FileSystemStorage


import requests

# Create your views here.

def home(request):

    return render(request,'core/home.html')


def carga(request):

    context = {}

    if request.method == 'POST':

        uploaded_file = request.FILES['document']

        fs = FileSystemStorage()

        name = fs.save(uploaded_file.name, uploaded_file)

        uploaded_file_url = fs.url(name)

        context['url'] = fs.url(name)

    return render(request,'core/carga.html',context)


def rxml(request):

    context = {}

    xml_file = open('media/entrada.xml')

    viewxml = xml_file.read()

    context['data'] = viewxml

    return render(request,'core/rxml.html',context)


def prepararxml(request):

    archivo_xml = open("media/entrada.xml","r")

    lectura_xml = archivo_xml.read()

    r = requests.get('http://127.0.0.1:5000/ob_xml',data=lectura_xml)

    #print(r.text)

    html_response = "<h1>Ejemplo1</h1>"
    
    html_response += r.text
    
    html_response += "<p>Eso es el resultado del Ejemplo1</p>"
    
    return HttpResponse(html_response)




    #return render(request,'core/preparado.html')