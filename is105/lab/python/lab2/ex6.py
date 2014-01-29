# -*- coding: latin-1 -*-

import sys

# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001

def ascii8Bin(A):
	return '{0:08b}'.format(ord(A))


def transferBin(string): 
	l = list(string)
	for c in l:
		print ascii8Bin(c)


print transferBin("Hi")
		# skriv ut den binere representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
