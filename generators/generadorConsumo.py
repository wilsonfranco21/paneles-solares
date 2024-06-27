import random
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["sony","LG","toyota"])
        capacidad=random.randint(100,2000) 
        ciudad=random.choice(["Medellin","Envigado","Cali","Amazonas","Bello"])
        responsable=random.choice(["wilson","Jose","Juan","Santiago","Johana"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos 
print(generarDatos())