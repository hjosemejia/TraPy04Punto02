"""
****************** TRABAJO SOBRE PYTHON ******************
"""

import os
global dagenda
global tagenda
global lagenda
global dagen
global prueba
dagenda = {}
tagenda = ()
lagenda = []
dagen = {}
prueba = 0

def presentacion():
    os.system("cls")
    print("****************************************")
    print("|** TRABAJO DE BASE DE DATOS AVANZADA **")
    print("|                                      |")
    print("|          JORGE ACOSTA PERTUZ         |")
    print("|           HECTOR MEJIA BUENO         |")
    print("|          MOISES RAMIREZ MARIN        |")
    print("|                                      |")
    print("|     ING. JAIDER QUINTERO MENDOZA     |")
    print("|               DOCENTE                |")
    print("|                                      |")
    print("|             UNIGUAJIRA               |")
    print("|       FACULTAD DE INGENIERIA         |")
    print("|        PROGRAMA DE SISTEMAS          |")
    print("|        DISTRITO DE RIOHACHA          |")
    print("|                2020                  |")
    print("|______________________________________|")

class Agenda():
    def __init__(self):
        varia = int(len(lagenda))
        x = 0
        print("********** INGRESAR CONTACTOS **********")
        print("")
        if varia == 0:
            self.nombre = input("NOMBRE DEL CONTACTO => ")
            self.telefono = int(input("CELULAR => "))
            self.email = input("E - MAIL => ")
            tagenda = (self.nombre, self.telefono, self.email)
            agenda = list(tagenda)
            lagenda.append(agenda)
        else:
            name  = input("NOMBRE DEL CONTACTO => ")
            while x < varia:
                tagenda = lagenda[x]
                self.nombre  = tagenda[0]
                if name in self.nombre:
                    print("NOMBRE YA EXISTE")
                    x = varia + 1
                    romper = 1
                else:
                    x += 1
                    romper = 0
            if  romper == 0:
                self.nombre = name
                self.telefono = int(input("CELULAR => "))
                self.email = input("E - MAIL => ")
                tagenda = (self.nombre, self.telefono, self.email)
                agenda = list(tagenda)
                lagenda.append(agenda)
    
        
    def ImprimirAgenda(self):
        print("********** IMPRIMIR CONTACTOS **********")
        print("")
        for x in range(len(lagenda)):
            tagenda = lagenda[x]
            print(f"CONTACTO {x+1}")
            self.nombre = tagenda[0]
            self.telefono = tagenda[1]
            self.email = tagenda[2] 
            print(f"NOMBRE => {self.nombre}")
            print(f"CELULAR => {self.telefono}")
            print(f"E-MAIL => {self.email}")
            print("")
    
    def ConsultarAgenda(self):
        print("********** BUSCAR CONTACTOS **********")
        print("")
        varia = int(len(lagenda))
        x = 0
        name = input("INGRESE EL NOMBRE DEL CONTACTO: ")
        while x < varia:
            tagenda = lagenda[x]
            self.nombre = tagenda[0]
            self.telefono = tagenda[1]
            self.email = tagenda[2]
            if name in self.nombre:
                print(f"NOMBRE => {self.nombre}")
                print(f"CELULAR => {self.telefono}")
                print(f"E - MAIL => {self.email}")
                prueba = x
                x += varia
            else:
                print("CONTACTO NO ENCONTRADO")
                x += 1
        return prueba
        
        
def menu():
    presentacion()
    os.system("pause")
    os.system("cls")
    while (True):
        print("****************************************")
        print("|************ __ M E N U __ ***********|")
        print("| 1. INGRESAR NEUVO CONTACTO           |")
        print("| 2. IMPRIMIR LOS CONTACTOS            |")
        print("| 3. CONSULTAR ALGUN CONTACTO          |")
        print("| 4. EDITAR ALGUN CONTACTO             |")
        print("| 5. SALIR DEL PROGRAMA                |")
        print("|______________________________________|")
        print("")
        opc = int(input("DIGITE LA OPCION QUE DESEA: "))
        if  opc == 1:
            agenda = Agenda()
        elif    opc == 2:
            agenda.ImprimirAgenda()
        elif    opc == 3:
            agenda.ConsultarAgenda()
        elif    opc == 4:
            pass
        elif    opc == 5:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break
        os.system("pause")
        os.system("cls")

def main():
    menu()

if __name__ == "__main__":
    main()