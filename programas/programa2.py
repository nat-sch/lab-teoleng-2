# -*- coding: utf-8 -*-
import re
import sys

def leer_pdf(ruta_pdf):
    from pypdf import PdfReader

    reader = PdfReader(ruta_pdf)
    pagina_factura = reader.pages[0]
    return pagina_factura.extract_text()

def get_fecha_monto(texto_factura):
    fecha_original = re.search(r'FECHA:\s*(\d*(-|/)\d*(-|/)\d*)', texto_factura).group(1)
    match = re.search(r'(\d{2})(-|/)(\d{2})(-|/)(\d{4})', fecha_original)
    dia = match.group(1)
    mes = match.group(3)
    anio = match.group(5)
    fecha = f"{anio}-{mes}-{dia}"

    monto = re.search(r'BANCARIO\s*(\d*,\d*)', texto_factura).group(1)
    return fecha, monto

def programa2(RutaFactura):
    return get_fecha_monto(leer_pdf(RutaFactura))
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
