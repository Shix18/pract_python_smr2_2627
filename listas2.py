notas = [7, 4.5, 9, 6, 10, 3, 8]

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Nota media:", sum(notas) / len(notas))

hay_suspenso = any(nota < 5 for nota in notas)
no_hay_ceros = all(nota != 0 for nota in notas)

print("¿Hay algún suspenso?", hay_suspenso)
print("¿No hay ningún cero?", no_hay_ceros)