import sys


#      '{0:08b}'.format(6)
#      00000110

def ascii8Bin(A):
	return '{0:08b}'.format(ord(A))

print ascii8Bin(6)
