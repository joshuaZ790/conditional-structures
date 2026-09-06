calificacion = float(input("Ingresa una calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    print("Calificación: A")
elif calificacion >= 80:
    print("Calificación: B")
elif calificacion >= 70:
    print("Calificación: C")
elif calificacion >= 60:
    print("Calificación: D")
elif calificacion >= 0:
    print("Calificación: F")
else:
    print("Calificación no válida.")


