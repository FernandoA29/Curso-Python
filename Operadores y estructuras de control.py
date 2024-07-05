"""
Operadores 
""" 

# Operadores aritméticos
print (f"Suma: 10 + 3 = {10 + 3}") 
print (f"Resta: 10 - 3 = {10 - 3}") 
print (f"Multiplicación: 10 * 3 = {10 * 3}") 
print (f"División: 10 / 3 = {10 / 3}") 
print (f"Módulo: 10 % 3 = {10 % 3}") 
print (f"Exponente: 10 ** 3 = {10 ** 3}") 
print (f"División entera: 10 // 3 = {10 // 3}") 

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 1 es {10 + 3 == 13 and 5 - 1 == 1}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")


"""
Estructuras de control 
""" 
# Condicionales

my_str = "Jose"

if my_str == "Fernando":
   print ("my_str es : 'Fernando'")
elif my_str == "Jose":
    print("my_str es 'Jose'")  
else:
    print("my_str no es :'Fernando'") 
       
# Iteractivas 
for i in range(11):
    print(i)
    
i = 0
while i <=10:
    print(i)
    i += 1    
       
# Manejo de excepciones 
try:
    print (10 / 0)   
except:
    print("Se ha producido un error")      
    
    
"""
Extra 
Crea un programa que imprima por consola todos los numeros comprendidos entre 10 y 55 (incluidos),
pares, y que no son ni el 16 ni multiplos de 3.
"""       
for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number % 3 !=0:
       print (number)