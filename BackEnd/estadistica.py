import xml.etree.ElementTree as ET

from lxml import etree

class estadistica:


    def w_xml(self,xmlfilesta,xmlfileprep):

        file = open(xmlfilesta,"w")

        file.write("<ESTADISTICAS>\n")

        xml_data = xmlfileprep

        tree = ET.parse(xml_data)

        root = tree.getroot()


        for elemento in root:

            file.write("<ESTADISTICA>\n")

            info = elemento.text + '#'

            indice = 0

            estado = 0

            straux = ""

            strauxrepor = ""

            strauxafec = ""

            strauxerr = ""

            while indice < len(info):

                letra = info[indice]

                if estado == 0:


                    if ord(letra) in range(48,58):

                        straux = straux + letra 

                        estado = 0

                    else:

                        if ord(letra) == 47:

                            straux = straux + letra

                            estado = 1

                            letra = " "
                        
                        else:

                            if(ord(letra)==82 or ord(letra)==114):

                                file.write("<REPORTADO_POR>"+'\n')

                                estado = 3

                                letra = " "
                            
                            else:

                                if ord(letra)==85 or ord(letra)==117:

                                    file.write("<AFECTADOS>"+'\n')

                                    estado = 12

                                    letra = " "

                if estado == 1:

                    if ord(letra) in range(48,58):

                        straux = straux + letra

                        estado = 1

                    else:

                        if ord(letra) == 47:

                            straux = straux + letra

                            estado = 2

                            letra = " "

                if estado == 2:

                    if ord(letra) in range(48,58):

                        straux = straux + letra 

                        estado = 2

                    else:

                        if letra == '\n':

                            file.write("<FECHA>"+straux+"</FECHA>"+'\n')

                            estado = 0
                
                if estado == 3:

                    if letra != ':':

                        #file.write(letra+"")

                        estado = 3

                    else:

                        estado = 4

                if estado == 4:

                    if letra == ':' or letra == " ":

                        estado = 4

                    else:
                            
                        if letra != ',' and letra != '\n':
                                
                            strauxrepor = strauxrepor + letra

                            #file.write(strauxrepor)
                        else:

                            if letra == ',':

                                estado = 5

                            if letra == '\n':

                                estado = 7
                                            
                if estado == 5:

                    file.write('<USUARIO>'+'\n'+'<EMAIL>'+strauxrepor+'</EMAIL>'+'\n'+'</USUARIO>'+'\n')

                    strauxrepor = ""

                    estado = 4
                
                if estado == 6:

                    file.write('<USUARIO>'+'\n'+'<EMAIL>'+strauxrepor+'</EMAIL>'+'\n'+'</USUARIO>'+'\n'+'</REPORTADO_POR>'+'\n')

                    strauxrepor = ""

                    estado = 0

                if estado == 7:

                    if letra == 'U':

                        estado = 6
                
                if estado == 8:

                    if letra == ':' or letra == " ":

                        estado = 8

                    else:
                            
                        if letra != ',' and letra != '\n':
                                
                            strauxafec = strauxafec + letra

                        else:

                            if letra == ',':

                                estado = 9

                            if letra == '\n':

                                estado = 11
                
                if estado == 9:

                    file.write('<AFECTADO>'+strauxafec+'</AFECTADO>'+'\n')

                    strauxafec = ""

                    estado = 8
                
                if estado == 10:

                    file.write('<AFECTADO>'+strauxafec+'</AFECTADO>'+'\n'+'</AFECTADOS>'+'\n')

                    strauxafec = ""

                    estado = 17
                
                if estado == 11:

                    if letra == 'E':

                        estado = 10

                if estado == 12:

                    if letra != ':':

                        estado = 12

                    else:

                        estado = 8

                if estado == 13:

                    if letra != ':':

                        estado = 13

                    else:

                        estado = 14

                if estado == 14:

                    if letra == ':' or letra == " ":

                        estado = 14

                    else:
                            
                        if ord(letra) in range(48,58) :
                                
                            strauxerr = strauxerr + letra

                        else:

                            if letra == '-':

                                estado = 15

                if estado == 15:

                    file.write('<ERROR>'+'\n'+'<CODIGO>'+strauxerr+'</CODIGO>'+'\n')

                    strauxerr = ""

                    estado = 16

                if estado == 16:

                    if letra == '-':

                        cant = 0

                    else:

                        if letra != '\n':

                            estado = 16

                        else:

                            estado = 18

                if estado == 17:

                    if ord(letra)==82 or ord(letra)==114:

                        file.write("<ERRORES>"+'\n')

                        estado = 13

                        letra = " "

                if estado == 18:

                    if letra == '\n':

                        cant = cant + 1

                        estado = 18

                    else: 
                        
                        if letra == '#':
                    
                            file.write('<CANTIDAD_MENSAJES>'+str(cant)+'</CANTIDAD_MENSAJES>'+'\n'+'</ERROR>'+'\n')
                    
                            estado = 0
                        
                        else:

                            estado = 16

                        
                indice += 1




            file.write("</ESTADISTICA>\n")




        file.write("</ESTADISTICAS>")


  
        file.close()
