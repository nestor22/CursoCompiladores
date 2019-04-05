import ply.yacc as yacc
import os
import codecs
import re
from analizador import tokens
from sys import stdin

precedence = (
('right', 'ASSIGN'),
('right', 'UPDATE'),
('left', 'NE'),
('left', 'LT', 'LTE', 'GT', 'GTE' ),
('left', 'PLUS', 'MINUS', 'DIVIDE'),
('right', 'ODD'),
('left', 'LPARENT', 'RPARENT')
)

def p_declaracion_asignar(p):
    '''declaracion : ID ASSIGN expresion'''
    print ("declaracion operador")

def p_declaracion_expr(p):
    '''declaracion : expresion'''
    # print("Resultado: " + str(t[1]))
    print ("declarracion exprecion")

def p_expresion_operaciones(p):
    '''
    expresion : expresion PLUSS expresion
                | expresion MINUS expresion
                | expresion TIME expresion
                | expresion DIVIDE expresion
    '''
    print ("operaciones")

def p_expresion_grupo(p):
    '''expresion  : LPARENT expresion RPARENT'''
    print ("agrupacion")

# sintactico de expresiones logicas
def p_expresion_logicas(p):
    '''
    expresion : expresion LT expresion
                | expresion GT expresion
                | expresion LTE expresion
                | expresion GTE expresion
                | expresion ASSIGN expresion
                | expresion NE expresion
                | LPARENT expresion RPARENT LT LPARENT expresion RPARENT
                | LPARENT expresion RPARENT GT LPARENT expresion RPARENT
                | LPARENT expresion RPARENT LTE LPARENT expresion RPARENT
                | LPARENT expresion RPARENT GTE LPARENT expresion RPARENT
                | LPARENT expresion RPARENT ASSIGN LPARENT expresion RPARENT
                | LPARENT expresion RPARENT NE LPARENT expresion RPARENT
    '''
    print ('expresion logica')

#
def p_expresion_numero(p):
    '''expresion : NUMBER'''
    print ("Number")

def p_expresion_nombre(p):
    '''expresion : ID'''
    print ("nombre")

def p_error(p):
    print ("error de sintasis", p)
    print ("error en la linea " + str(p.lineno))


def buscarFicheros(directorio):
    ficheros = []
    numArchivo=''
    respuesta = False
    cont =1
    for base, dirs, files in os.walk (directorio):
        ficheros.append(files)

    for file in files:
        print (str(cont)+". "+file)
        cont = cont+1
    while respuesta==False:
        numArchivo = input('\n Numero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta=True
                break
    print ("Has escogido \"%s\" \n "%files[int(numArchivo)-1])
    return files[int(numArchivo)-1]

directorio ='/home/salem/Documents/04 universidad/02-compiladores/03-GramaticasMasTablaSimbolos/pruebas/'
archivo = buscarFicheros(directorio)
test  = directorio+archivo
fp=codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()

result = parser.parse(cadena)

print (result)
