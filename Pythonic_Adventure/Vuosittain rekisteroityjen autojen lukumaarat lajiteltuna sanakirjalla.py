######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:25.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Tekstitiedoston automerkkien analysointi sanakirjan avulla
######################################################################
import sys

def paaohjelma():
    
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    vuosiLuvut = []
    vuosiLukuKirja = {}
    vuosiLuvut = LueTiedosto(luettavaTiedostoNimi)
    vuosiLukuKirja = ListaaTiedot(vuosiLuvut)
    
    if "empty" in vuosiLukuKirja:
        return None
    return None

def LueTiedosto(luettavaTiedostoNimi):
    vuosiLuvut = []

    try:
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        rivi = luettavaTiedosto.readline() 
        while(True):
            rivi = luettavaTiedosto.readline() 
            if (len(rivi) == 0):
               break
            rivi = rivi[:-1]
            rivi = rivi.split(";")
            rivi = rivi[1][0:4]
            vuosiLuvut.append(rivi)
        luettavaTiedosto.close()
   
    except:
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit()
   
    return vuosiLuvut

def ListaaTiedot(vuosiLuvut):
    
    vuosiLukuKirja = {}
    autoMaara = 0
    
    if (len(vuosiLuvut) == 0):
        print("Tiedosto oli tyhjä, yhtään autoa ei tunnistettu.")
        vuosiLuvuKirja["empty"] = 1

    else:
        vuosiLuvut.sort(reverse=True)
        for element in vuosiLuvut:
            if element in vuosiLukuKirja:
                vuosiLukuKirja[element] += 1
            else: 
                vuosiLukuKirja[element] = 1
        for element in vuosiLukuKirja:
            autoMaara += vuosiLukuKirja[element]

        print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
        print("Vuosi: Autoja")
        
        for element in vuosiLukuKirja:
            print("{0}: {1}".format(element, vuosiLukuKirja[element]))
        print("Yhteensä", autoMaara, "autoa.")
    
    return vuosiLukuKirja

paaohjelma()
print("Kiitos ohjelman käytöstä.")
