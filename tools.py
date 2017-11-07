import  math
import string
import sys
from __builtin__ import raw_input


Precedenti = {0:1L, 1:2L}


def Fibonaci2(n):
    if Precedenti.has_key(n):
        return Precedenti[n]
    else:
        nv = Fibonaci2(n-1)+Fibonaci2(n-2)
        Precedenti[n] = nv
        print nv
        return nv



def scambia(x,y):
    return y,x

def StampaParita(x):
    if x%2 == 0:
        print x," e par"
    else:
        print x," e impar"

def ControlloaRovecia(n):
    while n > 0:
        print n
        n = n-1

    print "partenza!"


def inserimentoText():
    text = raw_input("Dati inserito: ")
    print text

def AreaDellCerchio(raggio):
    return math.pi * raggio**2

def ValoreAssoluto(x):
    if x < 0:
        return -x
    elif x>0:
        return x

def DiztanzaTraDuePunti(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y1 - y2)**2 )

def Ipotenusa(cat1, cat2):
    return math.sqrt(cat1 ** 2 + cat2 ** 2)

def AreaaDellCerchio2(x1,y1,x2,y2):
    return AreaDellCerchio(DiztanzaTraDuePunti(x1,y1,x2,y2))

def Fatorial(n):
    if type(n) != type(1):
        print "Il fatoriale e' definito sole per valore inteiro"
        return -1
    elif n<0:
        print "Solo per numeri positivi"
        return -1
    elif n==0:
        return 1
    else:
       return n*Fatorial(n-1)

def Fibonaci(n):
    if type(n) != type(1):
        print "Il Fibonaci e' definito sole per valore inteiro"
        return -1
    elif n<0:
        print "Solo per numeri positivi"
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return Fibonaci(n-1)+Fibonaci(n-2)

def StampaMultiple(n,column):
    i = 1
    if column < 1:
        print "Deve avere al meno una coluna"
        return -1
    while i <=column:
        print n*i, '\t',
        i = i + 1
    print

def StampaTabela(riga,column):
    i = 1
    if riga < 1:
        print "al meno una riga"
        return -1
    while i<=riga:
        StampaMultiple(i,column)
        i = i + 1

def StringaRever(text):
    indice = (len(text)-1)
    while indice >= 0:
        lettera = text[indice]
        print lettera
        indice = indice - 1

def ExForIN():
    Prefissi = "JKLMNOPQ"
    Suffisso = "ack"
    for Lettera in Prefissi:
        print Lettera + Suffisso

def Trova(Stringa, Carattere,pos):
    Indice = pos
    while Indice < len(Stringa):
        if Stringa[Indice] == Carattere:
            return Indice
        Indice = Indice + 1
    return -1

def contaisIN(stringa,carattere):
    incremento = 0
    for carattere in stringa:
        if carattere == stringa:
            incremento = incremento+1

    return incremento

def scriveFile(file,text):
    f = open(file,"wr")
    f.write(text)
    f.close()
    print f
def imprimeTestoFile(file):
    f = open(file,"r")
    lista = f.readlines()
    imprimeLista(lista)

def imprimeLista(lista):
    i = 0
    while i < len(lista):
        print "[",i,"]",lista[i]
        if type(lista[i]) == type(lista) and type(lista) != type(""):
            imprimeLista(lista[i])
        i=i+1

def encontrarPosicao(lista, carattere):
    i = 0
    while i < len(lista):
        if lista[i]==carattere:
            return i
        i = i+1

def multSoma(x,y,z):
    return x*y+z
