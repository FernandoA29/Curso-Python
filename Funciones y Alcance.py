"""
Funciones definidas por el usuario
"""

# Simple

def greet():
    print("Hola, Python!")
    
greet()    

# Con retorno

def return_greet():
    return "Hola, Python!"

print(return_greet())

# Con un argumento

def arg_greet(name):
    print(f"Hola, {name}")
    
arg_greet("Fernando")    


# Con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}")
    
args_greet("Hi","Fernando")

# Con un argumento determinado

def default_arg_greet(name="Python"):
    print(f"Hola, {name}")
    
default_arg_greet("Fernando")
default_arg_greet()


# Con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}")   
    
variable_arg_greet("python", "Jose", "Fernando", "Ararat")


# Funciones del lenguaje (built - in)

print(len("Jose"))
print(type(5))
print("jose".upper())


# Variables locales y globales 

global_var = "Python"

print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")
    
hello_python()

# Extra

'''
crea una función que reciba dos parametros de tipo cadena de texto y retorne un numero.
- La función imprime todos los numeros del 1 al 100. Teniendo en cuenta que:
- Si el numero es multiplo de 3, muestra la cadena de texto del primer parametro.
- Si el numero es multiplo de 5, muestra la cadena de texto del segundo parametro.
- Si el numero es multiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el numero de veces que se ha impreso el numero en lugar de los textos.
'''

def print_number (text_1, text_2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print (text_1 + text_2)
        if number % 3 == 0:
            print (text_1)
        elif number % 5 == 0:
            print (text_2)    
        else:
            print(number)
            count += 1
    return count        
        
print (print_number("Texto 1", "Texto 2"))        

