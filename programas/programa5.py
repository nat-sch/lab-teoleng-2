# -*- coding: utf-8 -*-
import re
import sys

def leer_texto(ruta_pdf):
    from pypdf import PdfReader

    reader = PdfReader(ruta_pdf)
    pagina_factura = reader.pages[0]
    return pagina_factura.extract_text()

def get_fecha_monto(texto_factura):
    import re

    fecha_original = re.search(r'FECHA:\s*(\d*(-|/)\d*(-|/)\d*)', texto_factura).group(1)
    m = re.search(r'(\d{2})(-|/)(\d{2})(-|/)(\d{4})', fecha_original)
    dia = m.group(1)
    mes = m.group(3)
    anio = m.group(5)
    fecha = f"{anio}-{mes}-{dia}"

    monto = re.search(r'BANCARIO\s*(\d*,\d*)', texto_factura).group(1)
    return fecha, monto

def leer_xml(ruta_xml):
    return open(ruta_xml, 'r').read()

def hacer_patron_busca_linea(fecha_monto):
    fecha, monto = fecha_monto
    return rf'TipoMov="(D|C)".*Importe="{monto}".*Fecha="{fecha}"'

def programa5(RutaPdf,RutaXML):

    return bool(
        re.search(
            hacer_patron_busca_linea(
                get_fecha_monto(
                    leer_texto(RutaPdf)
                )
            ),
            leer_xml(RutaXML)
        )
    )

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
