#***************************
# manejo de listas
#***************************
def listas():
    lista1 = []
    lista2 = list()

    listaConElementos = [30, 2000000, "Sandra Daza", "Estudiante", True, ["Magister", "Doctorado", "Especializacion", 20]]

   # print(listaConElementos)

   # Utilizando el ciclo for
    for i in range(len(listaConElementos)):
       print(listaConElementos[i])
         
   # Utilizando el cilo while
    print("")
    print("")
    print("")
    print("Mostrando elementos con ciclo while")

    j=0
    while j < len(listaConElementos):
        print(listaConElementos[j])
        # j = j + 1
        j+=1

        listaConElementos[1] = listaConElementos[1] + 200000
    print(listaConElementos[5][3]) 
    print(listaConElementos[-1][3])
    print(listaConElementos[0:3]) # muestra la posicion de la 0 hasta la 3 sin entrar la 3 
    print(listaConElementos[0:6:2])  

    #listaConElementos.append(["Sede Riohacha", "Miguel Soto"]) - agrega elemento al final de la lista
    listaConElementos.insert(2,["Sede Riohacha", "Miguel Soto"]) # agrega elementos en la posicion x
    print(listaConElementos)

    del listaConElementos [2] # remover elementos en la posicion x
    print(listaConElementos)

    listaConElementos.remove("Estudiante")
    print(listaConElementos)



def main():
    listas()



if __name__ == "__main__":
    main()