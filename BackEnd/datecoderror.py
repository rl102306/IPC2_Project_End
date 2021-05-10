from nododatecodeerror import NodeDateCodeError


import matplotlib.pyplot as plt


class Listfilfce:



    def __init__(self):

        self.primero = None
        self.ultimo = None
    
    def vacia(self):

        if self.primero == None:

            return True

    def addInicio(self,codigo,fecha,cantidad):

        nuevo = NodeDateCodeError(codigo, fecha, cantidad)

        if self.vacia() == True:

            self.primero = self.ultimo = nuevo

            self.ultimo.siguiente = self.primero

        else:

            aux = NodeDateCodeError(codigo, fecha, cantidad)

            aux.siguiente = self.primero

            self.primero = aux

            self.ultimo.siguiente = self.primero

    def grafica(self,codigoerror):

        listax = []

        listay = []

        ejex = ""

        ejey = ""

        fig, ax, = plt.subplots()

        aux = self.primero

        while aux.siguiente != self.primero:

            if (codigoerror == aux.codigo):
        
                print("Codigo Erro : ", aux.codigo, "Fecha: ",aux.fecha, "Cantidad :" , aux.cantidad)

                listax.append(aux.fecha)

                listay.append(aux.cantidad)

            aux = aux.siguiente
        
        
        ax.scatter(listax,listay)

        plt.savefig('gfce.png')

        #plt.show()
        
        
        
        
        #print("Codigo Erro : ", aux.codigo, "Fecha: ",aux.fecha, "Cantidad :" , aux.cantidad)

    
