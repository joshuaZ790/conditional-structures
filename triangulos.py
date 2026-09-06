a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if a == b == c:
    print("El triángulo es equilátero.")
elif a == b or a == c or b == c:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
