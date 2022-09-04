#1. Smatraš da ste ti i tvoj simpatija suđeni? Napravi ljubavni kalkulator u programskom jeziku Python i saznaj!
from random import *
ime1=str(input('Unesi svoje ime: '))
ime2=str(input('Unesi ime simpatije: '))
print(ime1, 'i', ime2, 'zaljubljeni su',str(randrange(1,100)), '%')
