""""

Insertion sort é um algoritmo de ordenação que funciona da seguinte forma:

Começa com o primeiro elemento do array e assume que ele já está ordenado.
Em seguida, compara o segundo elemento com o primeiro. Se o segundo elemento for menor que o primeiro, ele é movido para a frente do array.
O processo é repetido para o terceiro elemento, o quarto elemento e assim por diante, até que todos os elementos tenham sido comparados.

"""

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            aux = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = aux

            j = j - 1


arr = [2,6,5,1,3,4]

insertion_sort(arr)
print(arr)