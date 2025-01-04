#---------------------------------Creando Clase donde se almacenaran todos los datos-----------------------------
"""
class Shopping_Kart:
    def __init__(self, nombre, cantidad, precio, sub_total, monto_iva, monto_total):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.sub_total = sub_total
        self.monto_iva = monto_iva
        self.monto_total = monto_total
"""

Shopping_Kart = {}
#-------------------------------------------Lista de productos con y sin IVA---------------------------------------

Lista_Iva = ["Alimentos básicos", "Medicamentos y productos de salud", "Material editorial y educativo",
             "Servicios básicos", "Electrodomésticos y tecnología", "Alimentos procesados y bebidas",
             "Bienes de lujo", "Bebidas alcoholicas"]

#--------------------------------------------Lista de opciones-----------------------------------------------------

Lista_Opciones = ["Si", "No", "No se"]

#------------------------------------------------Calculadora------------------------------------------------------

Calcular = "si"
id_item = int(1)

#sub_total = 0
#monto_iva = 0
#monto_total = 0

while Calcular == "si":

#-----------------------------------------------Imprimir lista de IVA-------------------------------------------

    i = 0
    while i < len(Lista_Iva):
        print(str(i+1) + ". " + Lista_Iva[i])
        i = i + 1

#----------------------------------------------Toma de datos del usuario---------------------------------------------

    categoria = int(input("Seleccione el numero de la categoria: "))
    categoria = categoria-1

    nombre = input("Nombre del producto: ")
    cantidad = float(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))

    print("¿El producto ya tiene el IVA agregado al precio?")

    i=0
    while i < len(Lista_Opciones):
        print(str(i+1) + ". " + Lista_Opciones[i])
        i = i + 1

    status = int(input("Seleccione el numero de las opciones: "))
    status = status-1

#-------------------------------------------Comienzo del proceso de Computo---------------------------------

    if status == 0:
        precio = precio/1.16
    
    if categoria > 3 and categoria <= 7:

        sub_total = precio * cantidad
        monto_iva = sub_total * 0.16
        monto_total = sub_total + monto_iva

    elif categoria <= 3 and categoria >= 0:
        
        sub_total = precio * cantidad
        monto_iva = 0
        monto_total = sub_total + monto_iva

    else:
        print("Número de categoria equivocado")


    Shopping_Kart[id_item] = {"nombre":nombre, "cantidad":cantidad, "precio":precio,
                              "sub_total":sub_total, "monto_iva":monto_iva, "monto_total":monto_total}

    id_item = id_item + 1

    Calcular = input("¿Quiere agregar otro producto? SI/NO: ").lower()



#-------------------------------------------------imprime los titulos-------------------------------------------
for clave_primaria in Shopping_Kart:
    for clave_secundaria in Shopping_Kart[clave_primaria]:
        print(clave_secundaria, end="\t")
    break

print("\n")

#-------------------------------------------------imprime los valores dentro del diccionario------------------------
    
for clave_primaria in Shopping_Kart:
    for clave_secundaria in Shopping_Kart[clave_primaria]:
        print(Shopping_Kart[clave_primaria][clave_secundaria], end="\t")

    print("\n")

#----------------------------------------------sumatoria de totales-----------------------------------
sub_total_sum = 0
monto_iva_sum = 0
monto_total_sum = 0
for clave_primaria in Shopping_Kart:
    sub_total_sum += Shopping_Kart[clave_primaria]["sub_total"]
    monto_iva_sum += Shopping_Kart[clave_primaria]["monto_iva"]
    monto_total_sum += Shopping_Kart[clave_primaria]["monto_total"]

print("SUB_TOTAL: " + str(sub_total_sum))
print("TOTAL DEL IVA: " + str(monto_iva_sum))
print("TOTAL DE LA COMPRA: " + str(monto_total_sum))
        