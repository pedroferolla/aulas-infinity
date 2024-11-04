# ATIVIDADE PRÁTICA 6

# Crie um programa que recebe dois conjuntos e exibe a interseção deles.

a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a.intersection(b))   # | Intersection() necessita ser feito a partir do comando 'print()'.

a.intersection_update(b)   # | Intersection_update() é feito para alteração antes e só depois é feito o comando 'print()'
print(a)
