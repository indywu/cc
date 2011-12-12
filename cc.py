#!/usr/bin/python
# -*- coding: utf-8 -*-

"""USAGE:
"""

__version__ = 0.03
__author__ = "Christine Tölzer"

""" Naechste Schritte:
in Webseite mit iframe einbinden
"""

def teilen(a, b):
    if a == 0:
        a = 1
    ergebnis4 = (1.0*a)/b 
    return ergebnis4


"""
print("Hallo Welt")
print("Bitte geben Sie die Gitterkonstanten ein")
a = input("a=")
b = input("b=")
c = input("c=")
print("Bitte geben Sie die Vervielfachung der Gitterkonstanten ein")
d = input("a=a*")
e = input("b=b*")
f = input("c=c*")
ergebnis = a * d
ergebnis2 = b * e
ergebnis3 = c * f
print("a= {0:.4f} b= {1:.4f} b= {2:.4f}".format(ergebnis, ergebnis2, ergebnis3) )
print("Bitte geben Sie die Positionen der Atome ein.")
print("Erstes Atom:")
x1 = input("x=")
y1 = input("y=")
z1 = input("z=")"""

print("{0:.4f}".format(teilen(0, 3)))
