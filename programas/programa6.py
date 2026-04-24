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

def leer_xml(ruta_xml):
    return open(ruta_xml, 'r').read()

def hacer_patron_busca_linea(fecha_monto):
    fecha, monto = fecha_monto
    return rf'.*TipoMov="(D|C)".*Importe="{monto}".*Fecha="{fecha}".*\n'

def programa6(RutaPdf,RutaXML):
    pat = hacer_patron_busca_linea(
        get_fecha_monto(
            leer_pdf(RutaPdf)
        )
    )

    xml_original = leer_xml(RutaXML)

    n_ocurrencias = len(re.findall(pat, xml_original))
    if n_ocurrencias > 0:
        nuevo_xml = re.sub(pat,'', xml_original)

        total_movimientos_viejo = int(
            re.search(r'<BanTeng:TotalMovimientos>\s*(\d+)\s*</BanTeng:TotalMovimientos>', xml_original).group(1)
        )
        total_movimientos_nuevo = total_movimientos_viejo - n_ocurrencias

        return re.sub(
            r'<BanTeng:TotalMovimientos>\s*(\d+)\s*</BanTeng:TotalMovimientos>',
            f'<BanTeng:TotalMovimientos>{total_movimientos_nuevo}</BanTeng:TotalMovimientos>',
            nuevo_xml
        )
    else:
        return xml_original



if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
