print()
print(" ===== PRECIO FINAL =====")
print(" AUTOR: LUIS SALOME ")
print()
#lectura de datos
PRECIO=float(input("Ingrese precio de venta, en dolares: "))
print()
#proceso
if PRECIO>300:
    PF=round(PRECIO*0.9,1)
    print(f"El monto a pagar es: {PF} dolares\n")
#fin