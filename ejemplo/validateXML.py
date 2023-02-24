# Ver http://pyjs.org/ y el Ãºltimo ejemplo de http://pyjs.org/examples/ (https://github.com/pyjs/pyjs/tree/master/examples/xmldoc/)
from lxml import etree

# Parsear el archivo XML
xml_file = etree.parse("datos_2.xml")

# Parsear la DTD
dtd = etree.DTD(open("datos_2.dtd"))

# Validar el archivo XML contra la DTD
def validate(xml_file, dtd):
    if dtd.validate(xml_file):
        print("El archivo es válido")
        #return ("True")
    else:
        print("El archivo NO es válido")
        #return ("False")

validate(xml_file, dtd)
