# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:06:01 2021

@author: acer
"""

soni=int(input("Bugun qancha odam bilan gaplashdingiz?>>" ) )

a= 'adfsfas'
print(a[3])
    
    
kimlar=[]
x = range(soni)
print(x)
for odam in list(range(soni)):
    kimlar.append(input(f' {odam+1}-suhbat qilgan odamingiz kim edi: '))


print(kimlar)
for ism in kimlar:
    print(ism)