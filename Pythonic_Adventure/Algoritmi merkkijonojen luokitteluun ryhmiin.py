######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:12.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
# COPY RIGHT
# Algoritmi merkkijonojen luokitteluun ryhmiin
######################################################################
import sys

def paaohjelma():
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    autoMerkit = []
    eriMerkit = []
    autoMerkit = LueTiedosto(luettavaTiedostoNimi)
    
    if "stop" in autoMerkit:
   
        sys.exit()
    
    eriMerkit = AnalysoiTiedot(autoMerkit)
    
    if "empty" in eriMerkit:
        
        return None
    virhe = TallennaTiedot(kirjoitettavaTiedostoNimi, eriMerkit)
    
    if (virhe == True):
       
        sys.exit()
    return None
    

def LueTiedosto(luettavaTiedostoNimi):
    autoMerkit = []
    try:
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        while(True):
            rivi = luettavaTiedosto.readline() 
            if (len(rivi) == 0):
                break
            autoMerkit.append(rivi)
        luettavaTiedosto.close()
    except:
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        
        autoMerkit.append("stop")
    
    return autoMerkit


def AnalysoiTiedot(autoMerkit):
    
    eriMerkit = []
    
    if (len(autoMerkit) == 0):
        
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
        
        eriMerkit.append("empty")
    else:
        
        for element in autoMerkit:
            
            if element not in eriMerkit:
                
                eriMerkit.append(element)
       
        print("Tiedostossa oli", len(eriMerkit), "eri automerkkiä.")
        
        for element in eriMerkit:
            print(element, end="")
    
    return eriMerkit


def TallennaTiedot(kirjoitettavaTiedostoNimi, eriMerkit):
   
    virhe = False
    try:
        
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        
        for element in eriMerkit:
            
            kirjoitettavaTiedosto.write(element)
        
        kirjoitettavaTiedosto.close()
    except:
        
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        
        virhe = True
    
    return virhe

paaohjelma()
print("Kiitos ohjelman käytöstä.")
