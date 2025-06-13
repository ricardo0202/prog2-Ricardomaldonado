# Pedimos al usuario un número entero
num_tabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"\n--- Tabla del {num_tabla} ---")

# Usamos un bucle for para generar la tabla del 1 al 10
for i in range(1, 11):  # range(1, 11) genera del 1 al 10
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")
