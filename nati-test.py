import os

os.system("mkdir /tmp/entradas")
os.system("mkdir /tmp/salidas")

def testear(n_programa):
    print(f"TESTANDO PROGRAMA {n_programa}")

    for i in range(5):
        os.system(f"cp entradas/factura{i+1}.pdf /tmp/entradas/factura{i+1}.pdf")
        os.system(f"cp salidas/programa{n_programa}_{i+1}.txt /tmp/salidas/programa{n_programa}_{i+1}.txt")

        os.system(f"python3 programas/programa{n_programa}.py entradas/factura{i+1}.pdf salidas/programa{n_programa}_{i+1}.txt")
        os.system(f"diff --strip-trailing-cr salidas/programa{n_programa}_{i+1}.txt salidas_esperadas/programa{n_programa}_{i+1}.txt")

        os.system(f"cp /tmp/entradas/factura{i+1}.pdf entradas/factura{i+1}.pdf")
        os.system(f"cp /tmp/salidas/programa{n_programa}_{i+1}.txt salidas/programa{n_programa}_{i+1}.txt")


testear(1)

os.system("rm -r /tmp/entradas")
os.system("rm -r /tmp/salidas")
