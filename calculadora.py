#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

if(len(sys.argv) != 4):
    print
    sys.exit("Usage: $ python calculadora.py function op1 op2")
else:
    try:
        if(sys.argv[1] == 'sumar'):
            print float(sys.argv[2])+float(sys.argv[3])
        elif(sys.argv[1] == 'restar'):
            print float(sys.argv[2])-float(sys.argv[3])
        elif(sys.argv[1] == 'dividir'):
            print float(sys.argv[2])/float(sys.argv[3])
        elif(sys.argv[1] == 'multiplicar'):
            print float(sys.argv[2])*float(sys.argv[3])
        else:
            print "Functions: sumar, restar, dividir, multiplicar"
    except ZeroDivisionError:
        print "Imposible division"
