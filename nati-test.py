import os

def testear(n_programa, ruta_xml=""):
    print(f"TESTANDO PROGRAMA {n_programa}")

    os.system("cp -r entradas /tmp")
    os.system("cp -r salidas /tmp")

    for i in range(5):
        print("="*10)

        os.system(f"python3 programas/programa{n_programa}.py entradas/factura{i+1}.pdf {ruta_xml} salidas/programa{n_programa}_{i+1}.txt")
        os.system(f"diff --strip-trailing-cr salidas/programa{n_programa}_{i+1}.txt salidas_esperadas/programa{n_programa}_{i+1}.txt")

        print("="*10)
    
    os.system("rm -r entradas")
    os.system("rm -r salidas")
    os.system("mv /tmp/entradas entradas")
    os.system("mv /tmp/salidas salidas")


testear(1)
testear(2)
testear(5, "entradas/TeoLeng6.xml")
testear(6, "entradas/TeoLeng6.xml")
