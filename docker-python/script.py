import time

#archivo = open("datos.txt","r")
#contenido = archivo.read()
contenido = 'datos.txt'
time_string = time.strftime("%H:%M:%S")

mydata=(time_string + " Hello world!")
    
n=3
while n >0:
    n=n-1
    with open(contenido, 'w', encoding='utf-8') as file_obj :
        file_obj.write(mydata)
        file_obj.close()


    with open("datos.txt","r") as archivo:
        contenido = archivo.read()

        print(contenido)