import xml.etree.ElementTree as ET

from flask import Flask,Response,request,jsonify

from lxml import etree

from preparar import preparar

from estadistica import estadistica

from datecoderror import Listfilfce

import re

import requests

import xmltodict


app  = Flask(__name__)


fileesta = estadistica()

@app.route('/')

def index():

    return'<h1>Hola Mundo</h1>'

@app.route('/events/',methods=['POST'])

def post_events():

    data = open('data.txt','w+')

    data.write(request.data.decode('utf-8'))

    data.close()

    return Response(response=request.data.decode('utf-8'),mimetype='text/plain',
                    content_type='text/plain')

@app.route('/events/', methods=['GET'])

def get_events():

    data = open('data.txt','r+')

    return Response(response=data.read(),mimetype='text/plain',
                    content_type='text/plain')

@app.route("/ob_xml",methods=['GET','POST'])

def envia_xml():

    # Recibe el XML como parametro

    xml_data = request.data

    #Escritura del XML Recibido

    archivo_xml = open("filepreparado.xml", "wb")

    archivo_xml.write(xml_data)

    archivo_xml.truncate()

    archivo_xml.close()

    

    #Prepara el archivo XML
        
    rutafile = 'filepreparado.xml'

    workxmlp = preparar()

    workxmlp.prep(rutafile)

    

    return "Archivo Procesado listo para consultar"

@app.route("/c_xml",methods=['GET','POST'])

def prepara_xml():

    ruta = 'estadistica.xml'

    xmlfile = 'filepreparado.xml'

    #fileesta = estadistica()

    fileesta.w_xml(ruta,xmlfile)

    # File Final

    datafilefinal = open('estadistica.xml','r+')

    return Response(response=datafilefinal.read(),mimetype='text/plain',
                    content_type='text/plain')



@app.route('/g_fce',methods=['GET','POST'])

def gfce():


    #fileesta.grafica(20001)

    fileesta.graficaest("20001")

    
    # Grafica por fech y por codigo de usuario



    datafilefinal = open('estadistica.xml','r+')

    return Response(response=datafilefinal.read(),mimetype='text/plain',
                    content_type='text/plain')
    



    

if __name__ == '__main__':

    app.run(debug=True,port=5000)

    workxmlp = preparar()

    
