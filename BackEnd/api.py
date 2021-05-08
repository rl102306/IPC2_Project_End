import xml.etree.ElementTree as ET

from flask import Flask,Response,request,jsonify

from lxml import etree

from preparar import preparar

import re

import requests

import xmltodict


app  = Flask(__name__)


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

    

        
    rutafile = 'filepreparado.xml'

    workxmlp = preparar()

    workxmlp.prep(rutafile)

    # Primer Limpieza XML

        # Limpia el nombre entre comillas del reportado por: 

    '''datafile = open(rutafile,'r+')

    data = datafile.read()

    datafile.seek(0)

    datafile.write(re.sub(r"\s<\"[a-zA-Z]*\s[a-zA-Z]*\s[0-9]*\"",r"", data))

    datafile.truncate()

    datafile.close()'''

    '''
    rutafile = 'filepreparado.xml'

    

    datafile = open(rutafile,'r+')

    data = datafile.read()

    datafile.close()

    
    datafile2 = open(rutafile,'w')

    datafile2.seek(0)

    

    datafile2.write(re.sub(r'\s<\"[a-zA-Z]*\s[a-zA-Z]*\s[0-9]*\"',r'', data))

    datafile2.truncate()

    
    datafile2.close()

    rutafile = 'filepreparado.xml'

    datafile = open(rutafile,'r+')

    data = datafile.read()

    datafile.seek(0)

    datafile.write(re.sub(r"\s<\"[a-zA-Z]*\s[a-zA-Z]*\s[0-9]*\"",r"", data))

    datafile.truncate()

    datafile.close()'''


    return "Archivo Procesado listo para consultar"

@app.route("/p_xml",methods=['GET','POST'])

def prepara_xml():

    print("")



@app.route('/w_xml',methods=['POST'])

def write_xml():

    # Primer Limpieza XML
    
    file = open("estadistica.xml","w")

    file.write("<ESTADISTICAS>\n")

    xml_data = 'entrada.xml'

    tree = ET.parse(xml_data)

    root = tree.getroot()


    for elemento in root:

        file.write("<ESTADISTICA>\n")

        info = elemento.text

        indice = 0

        estado = 0

        straux = ""

        while indice < len(info):

            letra = info[indice]

            if estado == 0:

                if ord(letra) in range(48,57):

                    straux = straux + letra 

                    estado = 0

                else:

                    if ord(letra) == 47:

                        straux = straux + letra

                        estado = 1

                        letra = " "

            if estado == 1:

                if ord(letra) in range(48,57):

                    straux = straux + letra

                    estado = 1

                else:

                    if ord(letra) == 47:

                        straux = straux + letra

                        estado = 2

                        letra = " "

            if estado == 2:

                if ord(letra) in range(48,57):

                    straux = straux + letra 

                    estado = 2

                else:

                    if letra == '\n':

                        file.write("<FECHA>"+straux+"</FECHA>"+"\n")

                        estado = 0

            indice += 1


        file.write("</ESTADISTICA>\n")


    file.write("</ESTADISTICAS>")


  
    file.close()

    # File Final

    datafilefinal = open('estadistica.xml','r+')

    return Response(response=datafilefinal.read(),mimetype='text/plain',
                    content_type='text/plain')
    



    

if __name__ == '__main__':

    app.run(debug=True,port=5000)

    workxmlp = preparar()
