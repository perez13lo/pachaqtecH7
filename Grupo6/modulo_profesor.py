import a_profesor
from menu import color


class Modulo_prof:
    def __init__(self,ans,conexion):
        self.ans=ans
        self.conexion=conexion
    
    def execute_modulo(self):
        if(self.ans=='1'): #read
            print("Ingrese el DNI del profesor:")
            DNI_profesor=input()
            query=a_profesor.funcion.find_profesor(DNI_profesor)
            record=self.conexion.find(query)
            print(record)
        elif(self.ans=='2'): #create
            print("Ingrese los datos del porfesor: ")
            DNI=input("DNI: ")
            Nombre_profesor=input("Nombre: ")
            Apellido_profesor=input("Apellido: ")
            query=a_profesor.funcion.insert_profesor(DNI,Nombre_profesor,Apellido_profesor)
            self.conexion.insert(query)
        elif(self.ans=='3'): #update
            print("Ingrese el DNI del prosor:")
            DNI_profesor=input("Respuesta: ")
            print("Ingrese el campo que desea modificar:")
            print("DNI➜ [1]           Nombre➜ [2]          Apellido➜ [3]")
            Field=input("Respuesta: ")
            if (Field=='1'):
                field="DNI"
            elif (Field=='2'):
                field="nombre"
            elif (Field=='3'):
                field="apellido"
            print("Ingrese el nuevo valor:")
            New_value=input("Respuesta: ")
            query=a_profesor.funcion.update_profesor_DNI(DNI_profesor)
            my_dict=a_profesor.funcion.update_profesor(New_value,field)
            self.conexion.update(query,my_dict)
        elif(self.ans=='4'): #delete
            print("Ingrese el DNI del profesor")
            DNI_profesor=input("")
            query=a_profesor.funcion.delete_profesor(DNI_profesor)
            self.conexion.delete(query)
        elif(self.ans=='9'):
            exit()

                