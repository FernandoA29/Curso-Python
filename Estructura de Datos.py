# Listas
"""
my_list = ["Fernando", "Carlos", "Juan", "Felipe", "Ricardo"] # creación lista
print(my_list)
my_list.append("Cristian") # Inserción
print(my_list)
my_list.remove("Juan") # Eliminar
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "Julian" # Actualización
print(my_list)
my_list.sort() # Ordenación
print(my_list)
"""
'''
import keyword
print(keyword.kwlist) # Muestra las palabras reservadas
'''
"""
crear una agenda de contactos por terminal.
- Debes implementar funcionalidades de busqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un numero de telefono.
- El programa solicita en primer lugar la operación que se quiere realizar, y a continuación los 
  datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir numeros de telefonos no numericos y con mas de 11 digitos.
  (o el numeros de digitos que quieras)
- Tambien se debe proponer una operación de finalización del programa.           
"""

def my_agenda():
  
  agenda = {}
  
  def insert_contact(): #definición de una función para no repetir codigo 
                        #(ya que es una mala practica de programación  )
      phone = input("Introduce el nuevo numero de contacto: ")
      if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
      else:
            print("Debes introducir un numero de telefono con menos de 12 digitos.")
  
  while True:
    
    print(" ")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    
    option = input(("\nSeleccione una opcion: "))
    
    match option:
      case "1":
        name = input("\nIntroduce el nombre del contacto a buscar: ")
        if name in agenda:
          print(f"El numero de teléfono de {name} es {agenda[name]}")  
        else:
          print(f"El contacto {name} no existe")  
      case "2":
        name = input("\nIntroduce el nombre del contacto: ")
        insert_contact()
      case "3":
        name = input("\nIntroduce el nombre del contacto a actualizar: ")
        if name in agenda:
          insert_contact()
        else:
          print("El contacto {name} no existe.")
      case "4":
        name = input("\nIntroduce el nombre del contacto a eliminar: ")
        if name in agenda:
          del agenda[name]
        else:
            print("El contacto {name} no existe. ")   
      case "5":
        print("Saliendo de la agenda.")
        break
      case _:
        print("Opción no valida. Elige una opción del 1 al 5.")
    
my_agenda()    