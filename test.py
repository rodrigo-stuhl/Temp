# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:15:46 2017

@author: rodrigo.stuhl
"""
tempstr1=""
tempstr2=""

fileResult = open('C:\Temp\RESULTADO.txt', 'w')

fileRead1 = open("C:\\Temp\\DWSD_FATO_ENCERRAMENTO_ANALISE_20150331.dat", 'r')
fileRead2 = open('C:\\Temp\\DWSD_ITEM_MEDICO_COBRADO_20150331.dat', 'r')
content1 = fileRead1.readlines()
content2 = fileRead2.readlines()
for i in range(len(content1)):
    tempstr1 = content1[i]
    tempstr2 = content2[i]
    if(tempstr1 == tempstr2[40:52]):
        fileResult.write(i + "\n")
        
fileRead1.close()
fileRead2.close()
fileResult.close()

print("FIM PROGRAMA: ")
