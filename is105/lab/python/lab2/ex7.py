# -*- coding: latin-1 -*-

import sys

#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#  

def ascii2Hex(A):
	return '{0:02x}'.format(ord(A))


def transferHex(string):
	l = list(string)
	for c in l:
		print ascii2Hex(c)


print transferHex("mno")
