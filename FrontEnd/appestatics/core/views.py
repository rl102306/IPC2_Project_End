from django.shortcuts import render , HttpResponse

from django.core.files.storage import FileSystemStorage

from os import remove,path

import requests




# Create your views here.

def home(request):

    return render(request,'core/home.html')


def carga(request):

    if path.exists("media/entrada.xml"):

         remove('media/entrada.xml')

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

    context = {}

    archivo_xml = open("media/entrada.xml","r")

    lectura_xml = archivo_xml.read()

    r = requests.get('http://127.0.0.1:5000/ob_xml',data=lectura_xml)

    #print(r.text)

    #html_response = "<h1>Ejemplo1</h1>"
    
    #html_response += r.text
    
    #html_response += "<p>Eso es el resultado del Ejemplo1</p>"

    context['ex'] = r.text
    
    return render(request,'core/preparado.html',context)


def wxml(request):

    context = {}

    #archivo_xml = open("media/entrada.xml","r")

    #lectura_xml = archivo_xml.read()

    r = requests.get('http://127.0.0.1:5000/c_xml')

    #print(r.text)

    #html_response = "<h1>Ejemplo1</h1>"
    
    #html_response += r.text
    
    #html_response += "<p>Eso es el resultado del Ejemplo1</p>"

    context['data'] = r.text
    
    return render(request,'core/estadisticas.html',context)


def grfce(request):

    if request.method == "POST":

        #response = ''

        codigo = request.POST['codigoerror']

        print("Hola soy del lado del front: " + codigo)

        r = requests.get('http://127.0.0.1:5000/g_fce', data=codigo)

    
    return render(request,'core/graficafce.html')

def ayuda(request):
    
    print("Hola")

    pdff = open('media/Ensayo3_201114493.pdf','rb')

    response = HttpResponse(pdff,content_type='application/pdf')

    return response
    
    return render(request,'core/ayuda.html')

    '''with open('media/Ensayo3_201114493.pdf', 'r',encoding="cp437", errors='ignore') as pdf:
        response = HttpResponse(pdf.read())
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed'''





