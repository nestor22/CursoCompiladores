import ply.lex as lex
import re
import codecs
import os
import sys



reservadas = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO',
             'CALL', 'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE'
]
tokens =reservadas+['ID','NUMBER', 'PLUS', 'MINUS', 'TIME', 'DIVIDE',
          'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
          'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM',
          'DOT', 'UPDATE'
]


#tokens = tokens+list(reservadas.values());

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIME = r'\*'
t_DIVIDE = r'/'
t_ODD = r'.'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
    r'[a-zA-Z_][a-zA-z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value

    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print ("carracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


analizador = lex.lex()
