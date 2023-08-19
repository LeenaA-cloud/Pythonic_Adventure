######################################################################
# Ohjelmoinnin perusteet
# Tekijä: Leena Pasanen
# Päivämäärä:14.7.2023
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
def LueTiedosto(luettavaTiedostoNimi):
    autoMerkki = []
    try:
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        while(True):
            rivi = luettavaTiedosto.readline() 
            if (len(rivi) == 0):
                break
            rivi = rivi[:-1]
            autoMerkki.append(rivi)
        luettavaTiedosto.close()
    except:
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit()
    return autoMerkki


def AnalysoiTiedot(autoMerkki):
    autoMerkkiLista = {}
    autoMaara = 0
    if (len(autoMerkki) == 0):
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
        autoMerkkiLista["empty"] = 1
    else:
        for element in autoMerkki:
            if element in autoMerkkiLista:
                autoMerkkiLista[element] += 1
            else: 
                autoMerkkiLista[element] = 1
        for element in autoMerkkiLista:
            autoMaara += autoMerkkiLista[element]
        print("Tunnistettiin", len(autoMerkkiLista), "automerkkiä ja", autoMaara, "autoa:")
        for element in autoMerkkiLista:
            if (autoMerkkiLista[element] == 1):
                print("{0}: {1} auto".format(element, autoMerkkiLista[element]))
            else:
                print("{0}: {1} autoa".format(element, autoMerkkiLista[element]))
    return autoMerkkiLista

def TallennaTiedot(kirjoitettavaTiedostoNimi, autoMerkkiLista):
    autoMaara = 0
    virhe = False
    try:
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        for element in autoMerkkiLista:
            autoMaara += autoMerkkiLista[element]
        kirjoitettavaTiedosto.write("Tunnistettiin {0} automerkkiä ja {1} autoa:\n".format(len(autoMerkkiLista), autoMaara))
        for element in autoMerkkiLista:
            if (autoMerkkiLista[element] == 1):
                kirjoitettavaTiedosto.write("{0}: {1} auto\n".format(element, autoMerkkiLista[element]))
            else:
                kirjoitettavaTiedosto.write("{0}: {1} autoa\n".format(element, autoMerkkiLista[element]))
        kirjoitettavaTiedosto.close()
    except:
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit()
    return virhe

def paaohjelma():
    
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    autoMerkki = []
    eriAutoMerkit = []
    autoMerkkiLista = {}
    autoMerkki = LueTiedosto(luettavaTiedostoNimi)
    autoMerkkiLista = AnalysoiTiedot(autoMerkki)
    
    if "empty" in autoMerkkiLista:
        
        return None
    
    TallennaTiedot(kirjoitettavaTiedostoNimi, autoMerkkiLista)
    return None

paaohjelma()
print("Kiitos ohjelman käytöstä.")
