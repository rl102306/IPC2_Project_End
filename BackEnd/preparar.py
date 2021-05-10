import xml.etree.ElementTree as ET

from lxml import etree

import re

class preparar():

    def prep(self,ruta):

      

        # Primer Limpieza XML

        # Limpia el nombre entre comillas del reportado por: 

        datafile = open(ruta,'r+')

        data = datafile.read()

        datafile.seek(0)

        datafile.write(re.sub(r"\s<\"[a-zA-Z]*\s[a-zA-Z]*\s[0-9]*\"",r"", data))

        datafile.truncate()

        datafile.close()

        
        
        
        
        # Segunda Limpieza XML

        # Limpia el ultimo > que queda en reportado por

        datafile2 = open(ruta,'r+')

        data2 = datafile2.read()

        datafile2.seek(0)

        datafile2.write(re.sub(r">\nU",r"\nU", data2))

        datafile2.truncate()


        datafile2.close()


        # Tercera Limpieza XML
        
        datafile3 = open(ruta,'r+')

        data3 = datafile3.read()

        datafile3.seek(0)

        datafile3.write(re.sub(r",\s<",r",", data3))

        datafile3.truncate()

        datafile3.close()

        # Cuarta Limpieza XML
        
        datafile4 = open(ruta,'r+')

        data4 = datafile4.read()

        datafile4.seek(0)

        datafile4.write(re.sub(r">,?\nE",r"\nE", data4))

        datafile4.truncate()

        datafile4.close()

        # Quinta Limpieza XML
        
        datafile5 = open(ruta,'r+')

        data5 = datafile5.read()

        datafile5.seek(0)

        datafile5.write(re.sub(r">,\s",r",", data5))

        datafile5.truncate()

        datafile5.close()

        # Sexta Limpieza XML
        
        datafile6 = open(ruta,'r+')

        data6 = datafile6.read()

        datafile6.seek(0)

        datafile6.write(re.sub(r"[A-Z][a-zA-Z]*,\s",r"", data6))

        datafile6.truncate()

        datafile6.close()


        # Septima Limpieza XML

        # La idea aca es quitar el < de usuarios afectados
        
        datafile7 = open(ruta,'r+')

        data7 = datafile7.read()

        datafile7.seek(0)

        datafile7.write(re.sub(r":\s<",r": ", data7))

        datafile7.truncate()

        datafile7.close()

    # Finaliza la limpieza para las estadisticas
