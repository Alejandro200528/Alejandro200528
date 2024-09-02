# lista = [3,5,4,7,8,23]
# tupla = (3,5,4,7,8,23)
# sets =  {3,5,4,7,8,23}
# direccionario = {'x':2,'y':4}

# lista [2]=12
# print(lista)

# lista =[3,5,4,7,8,32]
# fibo = []
# fibo.append(7)
# print(fibo)

# lista=[3,5,4,7,8,23]
# fibo=[0,1]
# for i in range (9):
#      fibo .append(fibo[i]+fibo[i+1])
# print(fibo)

# numero=[]
# for i in range (5):
#     x=int(input("escriba el numero: "))
#     if x>10:
#         numero.append(x)
# print(numero)        

# ganadores=["calixio","ruperto","catarcia","calixto","calixto",
#            "plutarco","ruperto","calixto","ruperto","calixto"]
# vencedores=["gabriela","lindsay","andres","stephania","wilian","luz"]

# vencedores.sort()
# x=sorted(vencedores)
# print(x)

# print(ganadores.count("calixto"))
# podio=vencedores.Index("linday")
# if podio+1<3:
#     print(F"lindsay si estas en el poidio con el puesto {podio}")
# else:
#     print(f"lindsay  no esta esta en el podio{podio+1}")





# import random

# def lanzar_dado():
#     """ Función para simular el lanzamiento de un dado, devuelve un número aleatorio entre 1 y 6. """
#     return random.randint(1, 6)

# def contar_treses(lista_lanzamientos):
#     """ Función para contar cuántos '3' hay en una lista de lanzamientos. """
#     return lista_lanzamientos.count(3)

# lanzamientos_participante1 = []
# lanzamientos_participante2 = []

# num_lanzamientos = 5

# for _ in range(num_lanzamientos):
#     lanzamiento1 = lanzar_dado()
#     lanzamientos_participante1.append(lanzamiento1)
    
#     lanzamiento2 = lanzar_dado()
#     lanzamientos_participante2.append(lanzamiento2)


# treses_participante1 = contar_treses(lanzamientos_participante1)
# treses_participante2 = contar_treses(lanzamientos_participante2)

# if treses_participante1 > treses_participante2:
#     print("¡El participante 1 es el ganador con {} treses!".format(treses_participante1))
# elif treses_participante2 > treses_participante1:
#     print("¡El participante 2 es el ganador con {} treses!".format(treses_participante2))
# else:
#     print("¡Es un empate con {} treses para ambos participantes!".format(treses_participante1))

# import random
# mustafa=[]
# zeinep=[]
# for i in ragen(6):
#     mustafa.append(random.randint(1,6))
#     zeinep.append(random.randint(1,6))
# must=mustafa.count(3)
# zei=zeinep.count(3)

# print(mustafa)
# print(zeinep)