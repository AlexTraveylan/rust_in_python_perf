import ctypes
import random
import time
# Charger la bibliothèque dynamique compilée à partir de Rust
lib = ctypes.CDLL("./target/release/bubble.dll")

# Définir les types des paramètres de la fonction bubble_sort
lib.bubble_sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_size_t]
lib.bubble_sort.restype = None

# Définition initiale de la liste 'arr'
arr = [random.randint(1, 10000) for _ in range(50_000)]
arr_copy = arr.copy()

# Création d'un tableau d'entiers C à partir de la liste Python
# Cela corrige l'erreur précédente où 'arr' n'était pas défini avant son utilisation
arr_c = (ctypes.c_int * len(arr))(*arr)

# Appel de la fonction bubble_sort avec le tableau d'entiers C
start_time = time.perf_counter()
lib.bubble_sort(arr_c, len(arr))
end_time = time.perf_counter()

# Conversion du tableau C en liste Python pour l'affichage des résultats
# Cette opération affichera le tableau après qu'il ait été trié par la fonction Rust
print([value for value in arr_c])
print(f"Temps d'exécution: {end_time - start_time} secondes (Rust)")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Échanger les éléments
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Utilisation de la fonction bubble_sort définie en Python
start_time = time.perf_counter()
bubble_sort(arr_copy)
end_time = time.perf_counter()

print(f"Temps d'exécution: {end_time - start_time} secondes (Python)")

# Vérification que les deux tableaux triés sont identiques
print(all(a == b for a, b in zip(arr_c, arr_copy)))
