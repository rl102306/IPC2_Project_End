from nododatecodeerror import NodeDateCodeError


class Listfilfce:

    def __init__(self):

        self.primero = none
        self.ultimo = none
    
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
    
