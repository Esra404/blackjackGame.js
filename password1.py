import random
import os
sayilar=[0,1,2,3,4,5,6,7,8,9]
harfler=['a','b','c','d','e','s','r']
sembol=['@','!','?','&','$']
max_length=12
alfabe=sayilar+harfler+sembol
sifre=0
for x in range(max_length):
    sifre= sifre+random.choice(alfabe)    


print(sifre)