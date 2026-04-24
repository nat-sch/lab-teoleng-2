# -*- coding: utf-8 -*-
import re
import sys

def leer_pdf(ruta_pdf):
    from pypdf import PdfReader

    reader = PdfReader(ruta_pdf)
    pagina_factura = reader.pages[0]
    return pagina_factura.extract_text()

def programa1(RutaPdf):
    return leer_pdf(RutaPdf)


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
