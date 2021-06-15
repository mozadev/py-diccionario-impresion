diccionario = { }

nombre=input("ingrese el nombre:  ")
apellido=input("ingrese el apellido : ")
direccion=input("ingrese el direccion:  ")
telefono=int(input("ingrese telefono:"))

diccionario = {'nombre' : nombre, 'apellido' :apellido,'direccion' :direccion,'telefono' :telefono, }

print(diccionario['nombre']+" "+diccionario['apellido']+" vive en "+diccionario['direccion']+" y su telefono es "+str(diccionario['telefono']))
