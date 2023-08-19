######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:10.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:

#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Python-kirjastojen käyttö, math ja random
######################################################################
print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
import math
import random

def paaohjelma():
    while(True):
        print("Mitä haluat tehdä:\n1) Laskea ympyrän pinta-alan\n2) Arvata luvun\n0) Lopeta")
        valinta= int(input("Valintasi: "))
        if(valinta == 1):
            YmpyranAla()
        elif(valinta == 2):
            Arvaus()
        elif(valinta == 0):
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    return None

def YmpyranAla():
    sade = int(input("Anna ympyrän säde kokonaislukuna: "))
    pintaAla = math.pi * math.pow(sade, 2)
    print("Säteellä ", sade, " ympyrän pinta-ala on ", format(pintaAla, '.2f'), ".\n",sep="")
    return None

def Arvaus():
    random.seed(1)
    arpaLuku = random.randint(0, 1000)
    print("Arvaa ohjelman arpoma kokonaisluku.")
    arvausKayttaja = int(input("Anna kokonaisluku välillä 0-1000: "))
    laskuri = 0
    while(True):
        laskuri += 1
        if (arvausKayttaja > arpaLuku):
            print("Haettu luku on pienempi.")
        elif (arvausKayttaja < arpaLuku):
            print("Haettu luku on suurempi.")
        elif (arvausKayttaja == arpaLuku):
            print("Oikein! Käytit arvaamiseen", laskuri, "kierrosta.\n")
            break
        arvausKayttaja = int(input("Anna kokonaisluku välillä 0-1000: "))
    return None

paaohjelma()
print("Kiitos ohjelman käytöstä.")
        
