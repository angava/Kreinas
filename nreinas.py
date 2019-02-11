import random
import numpy
import numpy as np

def eval(cromosoma, Size):

    a = np.zeros((Size,Size))
    #damos valor a la matriz.
    posX = 0
    for j in cromosoma:
        a[j, posX] = 1
        posX = posX + 1
    #print a

    #ubicamos el primer elemento de la matriz.
    valorFunc = Size
    posX = 0
    for i in cromosoma:
        #Verticalmente siempre estamos garantizando una solucion, por la
        #conformacion del cromosoma.
        #verificamos la horizontal
        verHort = 0 #varaible que verifica que no haya nada horizontalmente.
        for j in cromosoma:
            if i == j: 
               verHort = verHort + 1
               if verHort == 2: 
                  valorFunc = valorFunc - 1
        #ahora miramos las diagonales, mas dificil de programar.
    ctrUno = 0
    while valorFunc <> 0 and ctrUno == 0:
       #Sumamos la diagonal principal

       for i in range(Size):
           suma1 = 0
           for j in range(Size):
               #Diagonal principal con las diagonales hacia abajo
               if i+j < Size:
                  suma1 = suma1 + a[i+j,j]
           if suma1 > 1: valorFunc = valorFunc - 1
           suma2 = 0
           for j in range(Size):
               #Diagonal hacia arriba
               if j+i < Size and i > 0: 
                  suma2 = suma2 + a[j, j+i]
           if suma2 > 1: valorFunc = valorFunc - 1
           suma3 = 0
           for j in range(Size):
               #segunda diagonal con mitad hacia arriba
               if (Size - 1 - j) >= 0 and j-i >= 0: 
                  suma3 = suma3 + a[j-i, Size -1 - j]
           if suma3 > 1: valorFunc = valorFunc - 1
           suma4 = 0
           for j in range(Size):
               #ultima diagonal hacia abajo.
               if (Size - j) >= 0 and j+i-1 < Size and j > 0 and i > 0: 
                  suma4 = suma4 + a[j+i-1, Size - j]
           if suma4 > 1: valorFunc = valorFunc - 1
       ctrUno = 1
    if valorFunc < 0: valorFunc = 0
    return valorFunc 

def main():

  N_reinas = 4
  Pob = 20


  #Evaluamos la poblacion
  Cromosomas = []
  for i in range(Pob):
      TempCromo = []
      contElement = 0
      for j in range(N_reinas):
          elemArreglo = random.randint(0, N_reinas-1)
          if contElement > 0: 
             while elemArreglo in TempCromo: 
                    elemArreglo = random.randint(0, N_reinas-1)                    
          TempCromo.append(elemArreglo)
          contElement = contElement + 1
      Cromosomas.append(TempCromo) 

  #Evaluamos los cromosomas.
  
  valorFunc = []
  while not (N_reinas in valorFunc):
        for i in Cromosomas:
            valorFunc.append(eval(i, N_reinas))
            if eval(i, N_reinas)  == N_reinas: 
               print "solucion", i
               a = np.zeros((N_reinas,N_reinas))
               #damos valor a la matriz.
               posX = 0
               for j in i:
                   a[j, posX] = 1
                   posX = posX + 1
               print a
            papa1 
            papa2
            papa3
            papa4
            


              
  print valorFunc 


if __name__ == '__main__':
    main()
